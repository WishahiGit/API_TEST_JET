# Import relevant modules
import pytest
import allure
import datetime
from allure_commons.types import AttachmentType

# Pytest hook that runs after each test to generate the test report.
# If the test fails, it attaches the last API request and response details to the Allure report (if available).
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Check if this is the actual test execution phase and the test has failed
    if report.when == "call" and report.failed:
        # Try to get the API client from the test instance
        api_client = getattr(item.instance, "users_api", None)
        if api_client and hasattr(api_client, "last_response"):
            try:
                # Attach API request details (method, url, headers, payload, query params) to Allure
                allure.attach(
                    f"Method: {api_client.last_method}\n"
                    f"URL: {api_client.last_url}\n"
                    f"Headers: {api_client.last_headers}\n"
                    f"Payload: {getattr(api_client, 'last_payload', None)}\n"
                    f"Query Params: {getattr(api_client, 'last_qparams', None)}",
                    name=f"[{api_client.last_method}] request",
                    attachment_type=AttachmentType.TEXT
                )

                # Attach API response details (status, headers, body) to Allure
                response = api_client.last_response
                allure.attach(
                    f"Status: {response.status_code}\n"
                    f"Headers: {dict(response.headers)}\n"
                    f"Body: {response.text}",
                    name=f"response [{response.status_code}]",
                    attachment_type=AttachmentType.TEXT
                )
            except Exception as e:
                # If there is an error while attaching, log the error as well
                allure.attach(str(e), name="Allure Attachment Error", attachment_type=AttachmentType.TEXT)

# Another pytest hook to attach test start/end time and duration to Allure,
# and mark slow tests (>5s) as Critical severity in Allure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    # Record test start time
    start = datetime.datetime.now()
    allure.attach(start.strftime("%Y-%m-%d %H:%M:%S"),
                  name="⏰ Test Start Time", attachment_type=AttachmentType.TEXT)

    yield  # This runs the actual test

    # Record test end time and calculate duration
    end = datetime.datetime.now()
    duration = end - start
    seconds = duration.total_seconds()

    # Attach test end time and duration to Allure report
    allure.attach(end.strftime("%Y-%m-%d %H:%M:%S"),
                  name="🏁 Test End Time", attachment_type=AttachmentType.TEXT)

    allure.attach(f"{seconds:.2f} seconds",
                  name="⏱️ Test Duration", attachment_type=AttachmentType.TEXT)

    # If the test took longer than 5 seconds, mark it as CRITICAL severity and label it as slow in Allure
    if seconds > 5:
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.label("slow_test", "true")
