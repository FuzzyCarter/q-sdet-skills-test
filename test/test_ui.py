import pytest
from playwright.sync_api import Page, expect

class SubmitNameForm:
    def __init__(self, page: Page):
        self.page = page
        self.form = page.locator("#nameForm")
        self.input_name = page.locator("#name")
        self.submit_button = page.get_by_role("button")
        self.response_message = page.locator("#responseMessage")
        self.error_message = page.locator("#errorMessage")

    def submit_name(self, name: str):
        self.input_name.click()
        self.input_name.fill(name)
        self.submit_button.click()

    def get_response_message(self):
        return self.response_message.text_content()

    def get_error_message(self):
        return self.error_message.text_content()


def test_has_form(page: Page):
    page.goto("http://127.0.0.1:8080")
    form = SubmitNameForm(page)
    expect(form.form).to_be_visible()


def test_submit_name_success(page: Page):
    page.goto("http://127.0.0.1:8080")
    form = SubmitNameForm(page)
    form.submit_name("Alice")
    expect(form.response_message).to_have_text("Name submitted successfully: Alice")


def test_submit_name_missing_name(page: Page):
    page.goto("http://127.0.0.1:8080")
    form = SubmitNameForm(page)
    form.submit_name(" ")
    expect(form.error_message).to_have_text("Name is required.")


def test_submit_name_special_characters(page: Page):
    page.goto("http://127.0.0.1:8080")
    form = SubmitNameForm(page)
    form.submit_name("!@#$%^&*()_+")
    print(form.get_response_message())
    expect(form.response_message).to_have_text("Name submitted successfully: !@#$%^&*()_+")
