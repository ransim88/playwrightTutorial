
from playwright.sync_api import Playwright, sync_playwright
import pytest


@pytest.mark.regression
def atest_web_scrapper(playwright: Playwright) -> None:

    # Assess - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://mortgageafterlife.com/trending/que-fue-de-la-vida-de-los-actores-de-las-telenovelas-juveniles-de-cris-morena-algunos-de-ellos-lograron-consolidarse-otros-no-les-fue-nada-bien/?utm_source=taboola&utm_campaign=434334&utm_meidium=433443")

    # Act - When/And

    page.locator("text=SIGUIENTE➜").nth(1).click()

    # Assert - Then
    # assert page.is_visible("text=Revenue Report")


    # ---------------------
    context.close()
    browser.close()

