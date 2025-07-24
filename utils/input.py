import pandas as pd


def parse_bool(val):
    """
    Converts a string value to boolean.
    Accepts 'true', 'True', ' TRUE ', etc.
    Returns False for everything else.
    """
    return str(val).strip().lower() == "true"


def extract_id(data, fallback_id):
    """
    Extracts id from input data.
    If missing or invalid, uses fallback_id.
    """
    raw = data.get("id")
    if raw is None or str(raw).strip() == "":
        return fallback_id
    return int(float(raw))



def build_users_payload(data):
    """
    Builds a payload dictionary for creating or updating a user
    for the GoRest API based on provided input data.
    """
    return {
        "name": data.get("name", ""),
        "gender": data.get("gender", "").lower(),  # expected: "male" or "female"
        "email": data.get("email", ""),
        "status": data.get("status", "active").lower()  # typically "active" or "inactive"
    }
def build_post_payload(data):
    """
    Builds a payload dictionary for creating or updating a post
    for the GoRest API based on provided input data.
    """
    return {
        "title": data.get("title", "").strip(),
        "body": data.get("body", "").strip()
    }
