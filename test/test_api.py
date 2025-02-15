import pytest
from typing import Generator
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator:
    request_context = playwright.request.new_context(base_url="http://127.0.0.1:5000")
    yield request_context
    request_context.dispose()

def test_submit_name_success(api_request_context: APIRequestContext):
    response = api_request_context.post("/submit-name", data={"name": "Alice"})
    assert response.status == 200
    response_json = response.json()
    assert response_json["message"] == "Name submitted successfully: Alice"

def test_submit_name_missing_name(api_request_context: APIRequestContext):
    response = api_request_context.post("/submit-name", data={})
    assert response.status == 400
    response_json = response.json()
    assert response_json["error"] == "Name is required"

def test_submit_name_waldo(api_request_context: APIRequestContext):
    response = api_request_context.post("/submit-name", data={"name": "Waldo"})
    assert response.status == 403
    response_json = response.json()
    assert response_json["error"] == "You aren't Waldo - a real Waldo wouldn't reveal their identity!"
