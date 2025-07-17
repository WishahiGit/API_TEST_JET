from apis.BaseRequest import BaseRequest

class BooksAPI(BaseRequest):

    def __init__(self, base_url=None, default_headers=None):
        super().__init__()
        self.base_url = base_url or "http://localhost:5000"
        self.default_headers = default_headers or {
            "Content-Type": "application/json"
        }

    def get_books(self, headers=None):
        headers = headers or self.default_headers
        url = f"{self.base_url}/books"
        return self.get(url, headers=headers)

    def add_book(self, payload=None, headers=None):
        headers = headers or self.default_headers
        url = f"{self.base_url}/books"
        payload = payload or {}
        return self.post(url, headers=headers, payload=payload)

    def update_book(self, book_id, payload=None, headers=None):
        headers = headers or self.default_headers
        url = f"{self.base_url}/books/{book_id}"
        payload = payload or {}
        return self.put(url, headers=headers, payload=payload)

    def delete_book(self, book_id, headers=None):
        headers = headers or self.default_headers
        url = f"{self.base_url}/books/{book_id}"
        return self.delete(url, headers=headers)

    def get_users(self, headers=None):
        headers = headers or self.default_headers
        url = f"{self.base_url}/users"
        return self.get(url, headers=headers)

    def borrow_book(self, user_id, book_id, headers=None):
        headers = headers or self.default_headers
        url = f"{self.base_url}/users/{user_id}/borrow/{book_id}"
        return self.post(url, headers=headers)

    def return_book(self, user_id, book_id, headers=None):
        headers = headers or self.default_headers
        url = f"{self.base_url}/users/{user_id}/return/{book_id}"
        return self.post(url, headers=headers)
