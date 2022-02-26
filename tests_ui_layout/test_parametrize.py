import pytest
from playwright.sync_api import Playwright, sync_playwright

from pom.login_elements import LoginPage


@pytest.mark.parametrize("username", ["dev"])# pytest.param("kuku", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["6WQGUE5ZSzyK9Rqf"]) #, pytest.param("kuku", marks=pytest.mark.xfail)])
def atest_login_params(set_up, username, password) -> None:
    # Assess - Given
    page = set_up
    # Act - When/And
    page.fill("[aria-label='Username']", username)
    page.fill("[aria-label='Password']", password)
    if page.wait_for_selector("'Login'"):
        page.click("'Login'")

    page.wait_for_timeout(11000)
    if page.wait_for_selector("#sidebar button"):
        page.click("#sidebar button")
    with page.expect_navigation():
        page.click("#logout")
    page.fill("[aria-label='Username']", username)
    page.locator("[aria-label='Username']").press("Tab")
    page.fill("[aria-label='Password']", password)
    page.locator("[aria-label='Password']").press("Enter")
    page.wait_for_timeout(5000)
    page.wait_for_selector('[class="toggle-menu fa fa-bars"]')
    page.click('button[class="toggle-menu fa fa-bars"]')
    page.wait_for_timeout(1000)
    page.click("text=Graphs")
    page.wait_for_load_state()


    # Assert - Then
    # page.wait_for_selector("text=Websites - RT")
    assert page.is_visible("text=Revenue Report")
    assert page.is_visible("text=Websites - Daily")
    assert page.is_visible("text=Websites - RT")
    assert page.is_visible("text=Graphs")
    assert page.is_visible("text=Trend Graph")
    assert page.is_visible("text=Hourly Graph")
    assert page.is_visible("text=User Profit")
    assert page.is_visible("text=Action Log")
    assert page.is_visible("text=Report Dynamic")
    assert page.is_visible("text=Automation Management")
    assert page.is_visible("text=Site Configuration")

    # ---------------------


