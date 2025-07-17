def parse_bool(val):
    """
    Converts a string value to boolean.
    Accepts 'true', 'True', ' TRUE ', etc.
    Returns False for everything else.
    """
    return str(val).strip().lower() == "true"


def extract_book_id(data, fallback_id):
    """
    Extracts book_id from input data.
    If missing or empty, uses fallback_id.
    """
    raw = data.get("book_id")
    return int(float(raw)) if str(raw).strip() else fallback_id


def build_book_payload(data):
    """
    Builds a payload dictionary for book creation or update.
    """
    return {
        "title": data.get("title", ""),
        "author": data.get("author", ""),
        "is_borrowed": parse_bool(data.get("is_borrowed")),
    }
