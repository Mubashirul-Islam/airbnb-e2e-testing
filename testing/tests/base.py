import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.airbnb.com/")

    page.get_by_test_id("structured-search-input-field-query").click()
    page.get_by_test_id("structured-search-input-field-query").fill("Bangkok")
    expect(page.get_by_role("listbox", name="Search suggestions")).to_be_visible()

    page.get_by_role("button", name="When Add dates").click()
    page.get_by_role("button", name="Move forward to switch to the").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Move forward to switch to the").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Move forward to switch to the").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Move forward to switch to the").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Move forward to switch to the").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="12, Sunday, July 2026.").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="18, Saturday, July 2026.").click()
    page.wait_for_timeout(1000)
    expect(page.get_by_role("search")).to_contain_text("Jul 12 - 18")

    page.get_by_role("button", name="Who Add guests").click()
    expect(page.locator(".p1tlhulc")).to_be_visible()
    page.get_by_test_id("stepper-adults-increase-button").click()
    page.get_by_test_id("stepper-adults-increase-button").click()
    page.get_by_test_id("stepper-children-increase-button").click()
    page.get_by_test_id("stepper-infants-increase-button").click()
    page.get_by_test_id("stepper-pets-increase-button").click()
    expect(page.get_by_role("search")).to_contain_text("3 guests, 1 infant, 1 pet")

    page.get_by_test_id("structured-search-input-search-button").click()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
