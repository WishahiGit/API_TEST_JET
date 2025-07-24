import requests

class BaseRequest:

    def __init__(self):
        self.base_url = "https://gorest.co.in/public/v2"
        self.token = "c95841d6d1fda4a9e1494f2bddd6e6d69c48d2a8c006c1987a339e23a4a0afd5"
        self.default_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        self.last_method = None
        self.last_url = None
        self.last_headers = None
        self.last_payload = None
        self.last_qparams = None
        self.last_response = None

    def get(self, url, headers=None, params=None):
        headers = headers or self.default_headers
        self.last_method = "GET"
        self.last_url = url
        self.last_headers = headers
        self.last_qparams = params

        res = requests.get(url, headers=headers, params=params)
        self.last_response = res
        return res

    def post(self, url, headers=None, payload=None):
        headers = headers or self.default_headers
        self.last_method = "POST"
        self.last_url = url
        self.last_headers = headers
        self.last_payload = payload

        res = requests.post(url, headers=headers, json=payload)
        self.last_response = res
        return res

    def put(self, url, headers=None, payload=None):
        headers = headers or self.default_headers
        self.last_method = "PUT"
        self.last_url = url
        self.last_headers = headers
        self.last_payload = payload

        res = requests.put(url, headers=headers, json=payload)
        self.last_response = res
        return res

    def delete(self, url, headers=None):
        headers = headers or self.default_headers
        self.last_method = "DELETE"
        self.last_url = url
        self.last_headers = headers

        res = requests.delete(url, headers=headers)
        self.last_response = res
        return res
