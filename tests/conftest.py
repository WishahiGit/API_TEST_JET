import pytest
import allure
import datetime
from allure_commons.types import AttachmentType

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        api_client = getattr(item.instance, "users_api", None)
        if api_client and hasattr(api_client, "last_response"):
            try:
                allure.attach(
                    f"Method: {api_client.last_method}\n"
                    f"URL: {api_client.last_url}\n"
                    f"Headers: {api_client.last_headers}\n"
                    f"Payload: {getattr(api_client, 'last_payload', None)}\n"
                    f"Query Params: {getattr(api_client, 'last_qparams', None)}",
                    name=f"[{api_client.last_method}] request",
                    attachment_type=AttachmentType.TEXT
                )

                response = api_client.last_response
                allure.attach(
                    f"Status: {response.status_code}\n"
                    f"Headers: {dict(response.headers)}\n"
                    f"Body: {response.text}",
                    name=f"response [{response.status_code}]",
                    attachment_type=AttachmentType.TEXT
                )
            except Exception as e:
                allure.attach(str(e), name="Allure Attachment Error", attachment_type=AttachmentType.TEXT)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    start = datetime.datetime.now()
    allure.attach(start.strftime("%Y-%m-%d %H:%M:%S"),
                  name="⏰ Test Start Time", attachment_type=AttachmentType.TEXT)

    yield

    end = datetime.datetime.now()
    duration = end - start
    seconds = duration.total_seconds()

    allure.attach(end.strftime("%Y-%m-%d %H:%M:%S"),
                  name="🏁 Test End Time", attachment_type=AttachmentType.TEXT)

    allure.attach(f"{seconds:.2f} seconds",
                  name="⏱️ Test Duration", attachment_type=AttachmentType.TEXT)

    if seconds > 5:
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.label("slow_test", "true")
