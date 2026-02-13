from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, input_info: str):
        self.page.locator(locator).fill(input_info)

    def be_visible(self, locator: str):
        expect(self.page.locator(locator)).to_be_visible()

    def has_text(self, locator: str, text: str):
        expect(self.page.locator(locator)).to_have_text(text)
