def assert_common_fields(data):
    """
    Validates known fields if they exist.
    Does NOT require all fields to be present.
    """

    if "id" in data:
        assert isinstance(data["id"], int), "'id' must be int"

    if "title" in data:
        assert isinstance(data["title"], str), "'title' must be a string"
        assert data["title"].strip() != "", "'title' must not be empty"

    if "author" in data:
        assert isinstance(data["author"], str), "'author' must be a string"
        assert data["author"].strip() != "", "'author' must not be empty"

    if "is_borrowed" in data:
        assert isinstance(data["is_borrowed"], bool), "'is_borrowed' must be a boolean"

    if "message" in data:
        assert isinstance(data["message"], str), "'message' must be a string"
        assert data["message"].strip() != "", "'message' must not be empty"


def validate_response(res, expected):
    """
    Validates the HTTP response status and JSON fields for single-object responses.
    """
    if expected:
        assert res.status_code in [200, 201], f"Expected 200/201, got {res.status_code}"
        try:
            data = res.json()
        except Exception as e:
            raise AssertionError(f"Response is not valid JSON: {e}")
        assert_common_fields(data)
    else:
        assert res.status_code in [400, 404], f"Expected 400/404, got {res.status_code}"


def validate_list_response(res, expected, item_name="item"):
    """
    Validates JSON response for a list of items (e.g., books, users).
    Checks that each item has the required fields.
    """
    if expected:
        assert res.status_code in [200, 201], f"Expected 200/201, got {res.status_code}"
        try:
            data = res.json()
        except Exception as e:
            raise AssertionError(f"Response is not valid JSON: {e}")
        assert isinstance(data, list), f"Expected list of {item_name}s, got {type(data).__name__}"
        for item in data:
            assert isinstance(item, dict), f"Each {item_name} must be a dict"
            assert_common_fields(item)
    else:
        assert res.status_code in [400, 404], f"Expected 400/404, got {res.status_code}"
