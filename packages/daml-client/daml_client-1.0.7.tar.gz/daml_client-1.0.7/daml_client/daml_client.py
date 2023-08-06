import json
import logging
import time
import requests

REQUEST_OK = 200
REQUEST_INVALID_AUTH = 401
REQUEST_NOT_FOUND = 404
REQUEST_TOO_MANY_REQUESTS = 429
REQUEST_BAD_GATEWAY = 502
REQUEST_UNAVAILABLE = 503
REQUEST_GATEWAY_TIMEOUT = 504

party_token_map = dict()


class PartyToken:
    def __init__(self, token, timeout):
        self.token = token
        self.timeout = timeout


class DamlClient:

    def __init__(self, iam_url, auth_ledger_api, client_id, client_secret, ledger_id,
                 env='production', dr_iam_url='', dr_client_id='', dr_client_secret='', dr_ledger_id='',
                 logger=None, max_dr_retry_times=5, token_expired=12 * 60 * 60):
        """
        :param iam_url:             获取第三方平台token的url
        :param auth_ledger_api:     第三方平台 获取token需要的api地址参数
        :param client_id:           第三方平台 客户端ID
        :param client_secret:       第三方平台 客户端密钥
        :param ledger_id:           ledger账本 id
        :param env:                 当前环境
        :param dr_iam_url:          容灾模式下 获取第三方平台token的url
        :param dr_client_id:        容灾模式下 第三方平台 获取token需要的api地址参数
        :param dr_client_secret:    容灾模式下 第三方平台 客户端ID
        :param dr_ledger_id:        容灾模式下 第三方平台 客户端密钥
        :param logger:              自定义的logger
        :param max_dr_retry_times:  容灾模式下 最大重试时间
        :param token_expired:       token过期时间
        """
        # assert isinstance(iam_url, str)
        self.logger = logger if logger else logging.getLogger()
        self.token_expired = token_expired

        self.iam_url = iam_url
        self.dr_iam_url = dr_iam_url
        self.client_id = client_id
        self.dr_client_id = dr_client_id
        self.client_secret = client_secret
        self.dr_client_secret = dr_client_secret
        self.ledger_id = ledger_id
        self.dr_ledger_id = dr_ledger_id

        self.json_ledger_url = "https://{}." + env + ".dltsolutions.com.au/v1/"
        self.auth_ledger_api = auth_ledger_api

        self.max_dr_retry_times = max_dr_retry_times

        self.is_dr_mode = self.dr_iam_url and self.dr_client_id and self.dr_client_secret and self.dr_ledger_id
        self.error_status_code_list = [REQUEST_TOO_MANY_REQUESTS, REQUEST_BAD_GATEWAY, REQUEST_UNAVAILABLE,
                                       REQUEST_GATEWAY_TIMEOUT]

    def get_token_by_api(self, party, timeout=10, retry_times=0, is_dr_api=False):
        if is_dr_api:
            self.logger.debug('use dr point end')
        headers = {
            'content-type': 'application/json',
        }
        self.logger.debug(f"get token for {party}")
        data = {
            "client_id": self.dr_client_id if is_dr_api else self.client_id,
            "client_secret": self.dr_client_secret if is_dr_api else self.client_secret,
            "audience": self.auth_ledger_api,
            "grant_type": "client_credentials"
        }
        try:
            response = requests.post(self.dr_iam_url if is_dr_api else self.iam_url, headers=headers, json=data,
                                     timeout=timeout)
        except Exception as e:
            self.logger.exception(e)
            # 连接异常，直接切换容灾？
            if self.is_dr_mode and not is_dr_api:
                retry_times += 1
                if retry_times < self.max_dr_retry_times:
                    return self.get_token_by_api(party, timeout, retry_times, False)
                else:
                    return self.get_token_by_api(party, timeout, retry_times, True)
            else:
                raise e
        if response.status_code != REQUEST_OK:
            self.logger.debug(response.text)
            if not is_dr_api and (response.status_code in self.error_status_code_list or response.json().get(
                    'status') in self.error_status_code_list):
                # 429，需要等待更长时间
                time.sleep(1 if response.status_code == REQUEST_TOO_MANY_REQUESTS else 0.1)
                retry_times += 1
                if retry_times < self.max_dr_retry_times:
                    return self.get_token_by_api(party, timeout, retry_times, False)
                else:
                    return self.get_token_by_api(party, timeout, retry_times, True)
            raise Exception('request failed: ' + response.text)
        return json.loads(response.text).get('access_token')

    def reset_token(self, party):
        party_token_map[party] = PartyToken(self.get_token_by_api(party), int(time.time()))
        return party_token_map[party]

    def get_token(self, party):
        token = party_token_map.get(party, None)
        if not isinstance(token, PartyToken) or \
                int(time.time()) - token.timeout > self.token_expired:
            return self.reset_token(party).token
        return token.token

    def send_request_with_dr_point(self, party, method, data, timeout, retry_times=0, is_dr_api=False):
        """
        :param party: str           party的名称,例:   zerocap_client
        :param method: str          第三方平台请求方法的类型:   "create" or "exercise" or "query"
        :param data: dict           第三方平台请求方法的有效载荷数据
        :param timeout: int         延迟超时时间
        :param retry_times:         重试次数
        :param is_dr_api:           是否启用容灾
        :return:                    第三方平台 反回的response对象
        """
        if is_dr_api:
            self.logger.debug('use dr point end')

        headers = {
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'Authorization': f"Bearer {self.get_token(party)}"
        }

        asx_url = self.json_ledger_url.format(self.dr_ledger_id if is_dr_api else self.ledger_id)

        self.logger.debug('daml request: ' + asx_url + method)
        self.logger.debug('daml params: \n' + json.dumps(data, indent=4))
        try:
            response = requests.post(asx_url + method, headers=headers, json=data,
                                     timeout=timeout)

            if self.is_dr_mode and not is_dr_api and (response.status_code in self.error_status_code_list or
                                                      response.json().get('status') in self.error_status_code_list):
                # 429，需要等待更长时间
                time.sleep(5 if response.status_code == REQUEST_TOO_MANY_REQUESTS else 0.1)
                retry_times += 1
                if retry_times < self.max_dr_retry_times:
                    return self.send_request_with_dr_point(party, method, data, timeout, retry_times, False)
                else:
                    return self.send_request_with_dr_point(party, method, data, timeout, retry_times, True)
            return response
        except Exception as e:
            if self.is_dr_mode and not is_dr_api:
                return self.send_request_with_dr_point(party, method, data, timeout, retry_times, True)
            raise e

    def daml_request(self, method, data, party, timeout=10):
        """
        :param method: str          第三方平台请求方法的类型:   "create" or "exercise" or "query"
        :param data: dict           第三方平台请求方法的有效载荷数据
        :param party: str           party的名称,例:   zerocap_client
        :param timeout: int         延迟超时时间
        :return:
        """
        response = self.send_request_with_dr_point(party, method, data, timeout)

        if response.status_code == REQUEST_INVALID_AUTH or (
                response.status_code != REQUEST_OK and response.text.upper().find('UNAUTHENTICATED') >= 0):
            # 如果拿到的是没有认证的错误，重新获取token，然后重试
            self.reset_token(party)
            response = self.send_request_with_dr_point(party, method, data, timeout)
        self.logger.debug(response.text)
        return response


if __name__ == '__main__':

    daml_client = DamlClient(
        auth_ledger_api="https://zerocap.dltsolutions.com.au/ledger-api",
        iam_url="https://id.uat.dltsolutions.com.au/oauth/token",
        client_id="1MiDOUYfK0CgeAjUd0tuxu095nmnD1fy",
        client_secret="yX4NMrW3tuzYurj34V6mqnhWaf6sXTPO-XlNKI20PGX4Iv-D3qK3NwI-yjjuF_Z5",
        ledger_id="cg01j01",
        env='uat',
        dr_iam_url='',
        dr_client_id='wwxxyxYlRDwiWCYrCIlSHegATRGMt08c',
        dr_client_secret='mCn-V6ft884C6gC7jjZRDeSqnM5KP-Did8ioABmBlVzQT6EbBOqdTZJpe54gFXOZ',
        dr_ledger_id='',
        logger=None,
        max_dr_retry_times=5,
        token_expired=12 * 60 * 60
    )


    def get_all_data():
        """
        查询数据集
        :return:
        """
        payload_data = dict(templateIds=[
            '8e664e10953f3ab1b4dc8d8a4421f01d66402f1e0ad829de74a83c2203854b91:Address:Address',
            '8e664e10953f3ab1b4dc8d8a4421f01d66402f1e0ad829de74a83c2203854b91:Balance:Balance',
            '8e664e10953f3ab1b4dc8d8a4421f01d66402f1e0ad829de74a83c2203854b91:Rfq:Quote',
            '8e664e10953f3ab1b4dc8d8a4421f01d66402f1e0ad829de74a83c2203854b91:Rfq:Fill'
        ], query={})

        METHODS_DAML_QUERY = 'query'

        print(f"payload_data: >>>> {payload_data}")
        print(f"METHODS_DAML_QUERY: >>>> {METHODS_DAML_QUERY}")

        response = daml_client.daml_request(METHODS_DAML_QUERY, payload_data, "zerocap_client")
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception('400')


    print(get_all_data())
