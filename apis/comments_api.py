from apis.BaseRequest import BaseRequest

class commentsAPI(BaseRequest):
    def __init__(self):
        super().__init__()

    def get_all_comments(self, headers=None):
        url = f"{self.base_url}/comments"
        return self.get(url, headers=headers)

    def get_comment_by_id(self, comment_id, headers=None):
        url = f"{self.base_url}/comments/{comment_id}"
        return self.get(url, headers=headers)

    def create_comment(self, post_id, payload=None, headers=None):
        url = f"{self.base_url}/posts/{post_id}/comments"
        payload = payload or {}
        return self.post(url, headers=headers, payload=payload)

    def update_comment(self, comment_id, payload=None, headers=None):
        url = f"{self.base_url}/comments/{comment_id}"
        payload = payload or {}
        return self.patch(url, headers=headers, payload=payload)

    def delete_comment(self, comment_id, headers=None):
        url = f"{self.base_url}/comments/{comment_id}"
        return self.delete(url, headers=headers)
