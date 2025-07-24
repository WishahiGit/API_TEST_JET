from apis.BaseRequest import BaseRequest

class usersAPI(BaseRequest):
    def __init__(self):
        super().__init__()

    def get_all_userss(self, headers=None):
        url = f"{self.base_url}/users"
        return self.get(url, headers=headers)

    def get_users_by_id(self, id, headers=None):
        url = f"{self.base_url}/users/{id}"
        return self.get(url, headers=headers)

    def create_users(self, payload=None, headers=None):
        url = f"{self.base_url}/users"
        payload = payload or {}
        return self.post(url, headers=headers, payload=payload)

    def update_users(self, id, payload=None, headers=None):
        url = f"{self.base_url}/users/{id}"
        payload = payload or {}
        return self.put(url, headers=headers, payload=payload)

    def delete_users(self, id, headers=None):
        url = f"{self.base_url}/users/{id}"
        return self.delete(url, headers=headers)
