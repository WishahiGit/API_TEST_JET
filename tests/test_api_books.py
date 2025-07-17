import pytest
import allure

from utils.input import parse_bool, build_book_payload, extract_book_id
from utils.load_data import load_test_data
from tests.BaseTest import BaseTest
from utils.response_validators import validate_response, validate_list_response



@pytest.mark.api
@allure.epic("Books API")
class TestBooksAPI(BaseTest):
    created_ids = []

    @allure.description("Checks if the book list is empty when no books exist.")
    @pytest.mark.parametrize(*load_test_data("apis", "get_empty_books", parametrize=True))
    def test_get_empty_books(self, data):
        res = self.books_api.get_books()
        expected = parse_bool(data.get("expected"))
        validate_response(res, expected)

    @allure.description("Creates a new book and validates the response.")
    @pytest.mark.parametrize(*load_test_data("apis", "create", parametrize=True))
    def test_create_book(self, data):
        payload = build_book_payload(data)
        res = self.books_api.add_book(payload=payload)
        expected = parse_bool(data.get("expected"))

        validate_response(res, expected)
        if expected:
            self.__class__.created_ids.append(res.json()["id"])

    @allure.description("Fetches all books and validates their structure.")
    @pytest.mark.parametrize(*load_test_data("apis", "get_all_books", parametrize=True))
    def test_get_all_books(self, data):
        res = self.books_api.get_books()
        expected = parse_bool(data.get("expected"))
        validate_list_response(res, expected, item_name="book")

    @allure.description("Updates book details by book ID.")
    @pytest.mark.parametrize(*load_test_data("apis", "update_by_id", parametrize=True))
    def test_update_book(self, data):
        expected = parse_bool(data.get("expected"))
        try:
            book_id = extract_book_id(data, fallback_id=self.__class__.created_ids[0])
        except Exception:
            pytest.fail(f"[ERROR] Invalid book_id from Excel: '{data.get('book_id')}'")

        payload = build_book_payload(data)
        res = self.books_api.update_book(book_id, payload=payload)
        validate_response(res, expected)

    @allure.description("Fetches all users and validates their structure.")
    @pytest.mark.parametrize(*load_test_data("apis", "get_users", parametrize=True))
    def test_get_users(self, data):
        res = self.books_api.get_users()
        expected = parse_bool(data.get("expected"))
        validate_list_response(res, expected, item_name="user")

    @allure.description("Borrows a book by user and book ID.")
    @pytest.mark.parametrize(*load_test_data("apis", "borrow_book", parametrize=True))
    def test_borrow_book(self, data):
        expected = parse_bool(data.get("expected"))
        book_id = extract_book_id(data, fallback_id=self.__class__.created_ids[0])
        user = data.get("user")
        res = self.books_api.borrow_book(user, book_id)
        validate_response(res, expected)

    @allure.description("Returns a borrowed book.")
    @pytest.mark.parametrize(*load_test_data("apis", "return_book", parametrize=True))
    def test_return_book(self, data):
        expected = parse_bool(data.get("expected"))
        book_id = extract_book_id(data, fallback_id=self.__class__.created_ids[0])
        user = data.get("user")
        res = self.books_api.return_book(user, book_id)
        validate_response(res, expected)

    @allure.description("Deletes a book by ID.")
    @pytest.mark.parametrize(*load_test_data("apis", "delete_by_id", parametrize=True))
    def test_delete_book(self, data):
        expected = parse_bool(data.get("expected"))
        raw_id = data.get("book_id")
        book_id = int(raw_id) if raw_id else self.__class__.created_ids.pop(0)
        res = self.books_api.delete_book(book_id)
        validate_response(res, expected)
