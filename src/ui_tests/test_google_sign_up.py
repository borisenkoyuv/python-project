import json
from pathlib import Path

from playwright.sync_api import sync_playwright
import pytest

from pages.google_sign_in_page import GoogleSignInPage


class TestBaseSignUp:
    default_locale = "en-GB"
    texts = json.loads(Path("data/sign_in_texts.json").read_text(encoding="utf-8"))

    @pytest.fixture
    def page(self, request):
        locale = getattr(request, "language", self.default_locale)
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(channel="chrome", headless=True)
            context = browser.new_context(locale=locale)
            page = context.new_page()
            yield page
            context.close()
            browser.close()

    @pytest.mark.tc_id("TC-SIGN-IN-001")
    @pytest.mark.parametrize("page", [None], indirect=True)
    def test_language_change(self, page):
        sign_in_page = GoogleSignInPage(page)
        sign_in_page.open()
        sign_in_page.open_language_panel()
        sign_in_page.select_language("de")
        sign_in_page.is_title_present(self.texts["signin"]["title_de"])

    @pytest.mark.parametrize(
        "field_input, error",
        [
            ("", texts["signin"]["email_field"]["error_empty"]),
            ("test@gmail", texts["signin"]["email_field"]["error_invalid"]),
        ],
        ids=["TC-SIGN-IN-006", "TC-SIGN-IN-007"],
    )
    def test_incorrect_input(self, page, field_input, error):
        sign_in_page = GoogleSignInPage(page)
        sign_in_page.open()
        sign_in_page.enter_email(field_input)
        sign_in_page.click_next()
        sign_in_page.is_error_present(error)

    @pytest.mark.tc_id("TC-SIGN-IN-003")
    def test_check_forgot_email_link(self, page):
        sign_in_page = GoogleSignInPage(page)
        sign_in_page.open()
        sign_in_page.click_forgot_email()
        sign_in_page.is_forgot_email_field_present()
