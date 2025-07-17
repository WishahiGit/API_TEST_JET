import requests
import requests

class BaseRequest:

    def __init__(self):
        self.last_method = None
        self.last_url = None
        self.last_headers = None
        self.last_payload = None
        self.last_qparams = None
        self.last_response = None

    def get(self, url, headers=None, params=None):
        self.last_method = "GET"
        self.last_url = url
        self.last_headers = headers
        self.last_qparams = params

        res = requests.get(url, headers=headers, params=params)
        self.last_response = res
        return res

    def post(self, url, headers=None, payload=None):
        self.last_method = "POST"
        self.last_url = url
        self.last_headers = headers
        self.last_payload = payload

        res = requests.post(url, headers=headers, json=payload)
        self.last_response = res
        return res

    def put(self, url, headers=None, payload=None):
        self.last_method = "PUT"
        self.last_url = url
        self.last_headers = headers
        self.last_payload = payload

        res = requests.put(url, headers=headers, json=payload)
        self.last_response = res
        return res

    def delete(self, url, headers=None):
        self.last_method = "DELETE"
        self.last_url = url
        self.last_headers = headers

        res = requests.delete(url, headers=headers)
        self.last_response = res
        return res

