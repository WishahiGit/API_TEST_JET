def assert_common_fields(data):
    """
    Validates fields for GoRest user or post response.
    Determines the type of object based on available fields.
    """


    if "id" in data:
        assert isinstance(data["id"], int), "'id' must be an integer"
        assert data["id"] > 0, "'id' must be a positive integer"

    # ולידציה של משתמשים
    if "name" in data:
        assert isinstance(data["name"], str), "'name' must be a string"
        assert data["name"].strip(), "'name' must not be empty"

    if "email" in data:
        assert isinstance(data["email"], str), "'email' must be a string"
        assert "@" in data["email"], "'email' must contain '@'"

    if "gender" in data:
        assert data["gender"] in ["male", "female"], "'gender' must be 'male' or 'female'"

    if "status" in data:
        assert data["status"] in ["active", "inactive"], "'status' must be 'active' or 'inactive'"

    # ולידציה של פוסטים
    if "title" in data:
        assert isinstance(data["title"], str), "'title' must be a string"
        assert data["title"].strip(), "'title' must not be empty"

    if "body" in data:
        assert isinstance(data["body"], str), "'body' must be a string"
        assert data["body"].strip(), "'body' must not be empty"

    if "user_id" in data:
        assert isinstance(data["user_id"], int), "'user_id' must be an integer"
        assert data["user_id"] > 0, "'user_id' must be positive"


def validate_response(res, expected):
    """
    Validates the HTTP response status and JSON fields for single-object responses.
    """
    if expected:
        assert res.status_code in [200, 201, 204], f"Expected 200/201/204, got {res.status_code}"
        if res.status_code == 204:
            return
        if 'application/json' in res.headers.get('Content-Type', ''):
            try:
                data = res.json()
                assert_common_fields(data)
            except Exception as e:
                raise AssertionError(f"Response is not valid JSON: {e}")
        else:
            print(f"Non-JSON response body: {res.text}")
    else:
        assert res.status_code >= 400, f"Expected status code >= 400, got {res.status_code}"



def validate_list_response(res, expected, item_name="item"):
    """
    Validates JSON response for a list of items (e.g., users, books).
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
        assert res.status_code >= 400, f"Expected status code >= 400, got {res.status_code}"

