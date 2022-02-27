import time
import pytest
from playwright.sync_api import Playwright, sync_playwright

import utils
from utils import secret_config
from pom.login_elements import LoginPage


def test_login_page(login_set_up) -> None:

    # Assess - Given
    page = login_set_up
    login = LoginPage(page)
    login.login_form("dev", utils.secret_config.PASSWORD)


    # page.click(LoginPage.loginButton)
    assert page.is_visible(login.username_elem)
    assert page.is_visible(login.password_elem)


@pytest.mark.regression
def test_login_page_2(login_set_up) -> None:

    # Assess - Given
    page = login_set_up
    login = LoginPage(page)
    login.login_form("dev", "6WQGUE5ZSzyK9Rqf")


    # page.click(LoginPage.loginButton)
    assert page.is_visible(login.username_elem)
    assert page.is_visible(login.password_elem)

