from pages.base_page import BasePage


class GoogleSignInPage(BasePage):
    URL = "https://accounts.google.com/"
    EMAIL_PHONE_INPUT_FIELD = "#identifierId"
    NEXT_BUTTON = "#identifierNext"
    CHANGE_LANGUAGE = "div[role=combobox]"
    TITLE = "#headingText"
    EMAIL_PHONE_PHONE_ERROR = "#i8"
    FORGOT_EMAIL_BUTTON = "role=button[name='Forgot email?']"
    FORGOT_EMAIL_INPUT_FIELD = "#recoveryIdentifierId"


    def open(self):
        self.page.goto(self.URL)

    def enter_email(self, email: str):
        self.fill(self.EMAIL_PHONE_INPUT_FIELD, email)

    def click_next(self):
        self.click(self.NEXT_BUTTON)

    def open_language_panel(self):
        self.click(self.CHANGE_LANGUAGE)

    def select_language(self, language):
        self.click(f"li[data-value='{language}']")

    def is_title_present(self, text):
        self.has_text(self.TITLE, text)

    def is_error_present(self, text):
        self.has_text(self.EMAIL_PHONE_PHONE_ERROR, text)

    def click_forgot_email(self):
        self.click(self.FORGOT_EMAIL_BUTTON)

    def is_forgot_email_field_present(self):
        self.be_visible(self.FORGOT_EMAIL_INPUT_FIELD)
