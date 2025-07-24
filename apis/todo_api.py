from apis.BaseRequest import BaseRequest

class todosAPI(BaseRequest):
    def __init__(self):
        super().__init__()

    def get_all_todos(self, headers=None):
        url = f"{self.base_url}/todos"
        return self.get(url, headers=headers)

    def get_todo_by_id(self, todo_id, headers=None):
        url = f"{self.base_url}/todos/{todo_id}"
        return self.get(url, headers=headers)

    def create_todo(self, user_id, payload=None, headers=None):
        url = f"{self.base_url}/users/{user_id}/todos"
        payload = payload or {}
        return self.post(url, headers=headers, payload=payload)

    def update_todo(self, todo_id, payload=None, headers=None):
        url = f"{self.base_url}/todos/{todo_id}"
        payload = payload or {}
        return self.patch(url, headers=headers, payload=payload)

    def delete_todo(self, todo_id, headers=None):
        url = f"{self.base_url}/todos/{todo_id}"
        return self.delete(url, headers=headers)
