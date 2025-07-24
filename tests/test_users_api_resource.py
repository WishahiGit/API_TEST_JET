import pytest
import allure

from tests.BaseTest import BaseTest
from utils.input import parse_bool, build_users_payload, extract_id
from utils.load_data import load_test_data
from utils.response_validators import validate_response, validate_list_response


@pytest.mark.api
@allure.epic("users API")
class TestusersAPI(BaseTest):
    created_ids = []

    @allure.description("Checks if the users list is empty when no users exists.")
    @pytest.mark.parametrize(*load_test_data("apis", "get_empty_users", parametrize=True))
    def _test_get_empty_users(self, data):
        res = self.users_api.get_all_userss()
        expected = parse_bool(data.get("expected"))
        validate_response(res, expected)

    @pytest.mark.order(1)
    @allure.description("Creates a new users and validates the response.")
    @pytest.mark.parametrize(*load_test_data("apis", "create_user", parametrize=True))
    def test_create_users(self, data):
        payload = build_users_payload(data)
        res = self.users_api.create_users(payload=payload)
        expected = parse_bool(data.get("expected"))

        validate_response(res, expected)
        if expected:
            user_id = res.json()["id"]
            self.__class__.created_ids.append(user_id)
            print(f"\n[CREATE] User created with ID: {user_id}")

    @allure.description("Fetches all userss and validates their structure.")
    @pytest.mark.parametrize(*load_test_data("apis", "get_all_users", parametrize=True))
    def test_get_all_users(self, data):
        res = self.users_api.get_all_userss()
        expected = parse_bool(data.get("expected"))

        validate_list_response(res, expected, item_name="users")

    @allure.description("Updates users details by users ID.")
    @pytest.mark.parametrize(*load_test_data("apis", "update_by_id", parametrize=True))
    def test_update_users(self, data):
        expected = parse_bool(data.get("expected"))
        id = extract_id(data, fallback_id=self.__class__.created_ids[0])
        print(f"\n[UPDATE] Updating user with ID: {id}")

        payload = build_users_payload(data)
        res = self.users_api.update_users(id, payload=payload)

        validate_response(res, expected)

    @allure.description("Fetches a users by ID and validates the response.")
    @pytest.mark.parametrize(*load_test_data("apis", "get_by_id", parametrize=True))
    def test_get_by_id(self, data):
        expected = parse_bool(data.get("expected"))
        id = extract_id(data, fallback_id=self.__class__.created_ids[0])
        print(f"\n[GET] Getting user with ID: {id}")

        res = self.users_api.get_users_by_id(id)

        validate_response(res, expected)

    @allure.description("Deletes a users by ID.")
    @pytest.mark.parametrize(*load_test_data("apis", "delete_by_id", parametrize=True))
    def test_delete_users(self, data):
        expected = parse_bool(data.get("expected"))
        raw_id = data.get("id")
        id = int(raw_id) if raw_id else self.__class__.created_ids.pop(0)
        print(f"\n[DELETE] Deleting user with ID: {id}")

        res = self.users_api.delete_users(id)

        validate_response(res, expected)
