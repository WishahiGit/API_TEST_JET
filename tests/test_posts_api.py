import pytest
import allure

from tests.BaseTest import BaseTest
from utils.input import parse_bool, build_post_payload
from utils.load_data import load_test_data
from utils.response_validators import validate_response, validate_list_response


@pytest.mark.api
@allure.epic("posts API")
class _TestpostsAPI(BaseTest):
    created_post_ids = []

    @allure.description("Creates a post for the existing user and validates the response.")
    @pytest.mark.parametrize(*load_test_data("apis", "create_post", parametrize=True))
    def test_create_post(self, data):
        expected = parse_bool(data.get("expected"))

        assert hasattr(self, "users_api")
        assert self.users_api.__class__.created_ids, "No user ID available from users test."
        user_id = self.users_api.__class__.created_ids[0]
        print(f"\n[CREATE POST] Using user_id: {user_id}")

        payload = build_post_payload(data)

        res = self.posts_api.create_post(user_id, payload=payload)
        validate_response(res, expected)

        if expected and res.status_code == 201:
            post_id = res.json()["id"]
            self.__class__.created_post_ids.append(post_id)
            print(f"[CREATE POST] Created post ID: {post_id}")

    @allure.description("Fetches all posts and validates structure.")
    @pytest.mark.parametrize(*load_test_data("apis", "get_all_posts", parametrize=True))
    def test_get_all_posts(self, data):
        expected = parse_bool(data.get("expected"))
        res = self.posts_api.get_all_posts()
        validate_list_response(res, expected, item_name="posts")

    @allure.description("Fetches a post by ID and validates the response.")
    @pytest.mark.parametrize(*load_test_data("apis", "get_post_by_id", parametrize=True))
    def test_get_post_by_id(self, data):
        expected = parse_bool(data.get("expected"))
        post_id = data.get("id") or self.__class__.created_post_ids[0]
        print(f"\n[GET POST] Getting post ID: {post_id}")

        res = self.posts_api.get_post_by_id(post_id)
        validate_response(res, expected)

    @allure.description("Updates a post by ID.")
    @pytest.mark.parametrize(*load_test_data("apis", "update_post", parametrize=True))
    def test_update_post(self, data):
        expected = parse_bool(data.get("expected"))
        post_id = data.get("id") or self.__class__.created_post_ids[0]
        print(f"\n[UPDATE POST] Updating post ID: {post_id}")

        payload = build_post_payload(data)

        res = self.posts_api.update_post(post_id, payload=payload)
        validate_response(res, expected)

    @allure.description("Deletes a post by ID.")
    @pytest.mark.parametrize(*load_test_data("apis", "delete_post", parametrize=True))
    def test_delete_post(self, data):
        expected = parse_bool(data.get("expected"))
        post_id = data.get("id") or self.__class__.created_post_ids.pop(0)
        print(f"\n[DELETE POST] Deleting post ID: {post_id}")

        res = self.posts_api.delete_post(post_id)
        validate_response(res, expected)
