from playwright.sync_api import Playwright, sync_playwright

from testing.tests.test_search_location import test_search_location
from testing.tests.test_select_dates import test_select_dates
from testing.tests.test_add_guests import test_add_guests
from testing.tests.test_submit_search import test_submit_search
from testing.tests.test_item_details import test_item_details


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.airbnb.com/")
    

    test_search_location(page)
    page.wait_for_timeout(1000)

    selected_dates = test_select_dates(page)
    page.wait_for_timeout(1000)

    guests = test_add_guests(page)
    page.wait_for_timeout(1000)

    test_submit_search(page, selected_dates, guests)
    page.wait_for_timeout(1000)

    test_item_details(page)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
