from apis.BaseRequest import BaseRequest

class postsAPI(BaseRequest):
    def __init__(self):
        super().__init__()

    def get_all_posts(self, headers=None):
        url = f"{self.base_url}/posts"
        return self.get(url, headers=headers)

    def get_post_by_id(self, post_id, headers=None):
        url = f"{self.base_url}/posts/{post_id}"
        return self.get(url, headers=headers)

    def create_post(self, user_id, payload=None, headers=None):
        url = f"{self.base_url}/users/{user_id}/posts"
        payload = payload or {}
        return self.post(url, headers=headers, payload=payload)

    def update_post(self, post_id, payload=None, headers=None):
        url = f"{self.base_url}/posts/{post_id}"
        payload = payload or {}
        return self.patch(url, headers=headers, payload=payload)

    def delete_post(self, post_id, headers=None):
        url = f"{self.base_url}/posts/{post_id}"
        return self.delete(url, headers=headers)
