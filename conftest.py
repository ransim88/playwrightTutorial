import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="function")
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://preprod.skyneto.com/")
    page.set_default_timeout(2000)

    yield page
    page.close()


@pytest.fixture(scope="function")
def login_set_up(set_up):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page = set_up

    page.fill("[aria-label='Username']", "dev")
    page.fill("[aria-label='Password']", "6WQGUE5ZSzyK9Rqf")
    if page.wait_for_selector("'Login'"):
        page.click("'Login'")

    yield page
