from playwright.sync_api import Page, expect
import random


def test_search_location(page: Page) -> None:
    if page.get_by_role("button", name="Got it").is_visible():
        page.screenshot(path="screenshots/screenshot.png")
        page.get_by_role("button", name="Got it").click()
    page.get_by_test_id("structured-search-input-field-query").click()


    countries = ["United States", "Canada", "Mexico", "United Kingdom", "France", "Germany", "Spain", "Italy", "Australia", "Japan", 
                 "South Korea", "Thailand", "Singapore", "India", "Brazil", "Argentina", "Portugal", "Greece", "Bangladesh", "Netherlands"]
    selected_country = random.choice(countries)
    
    page.get_by_test_id("structured-search-input-field-query").type(selected_country)
    page.screenshot(path="screenshots/screenshot2.png")
    expect(page.get_by_role("listbox", name="Search suggestions")).to_be_visible()
    expect(page.get_by_test_id("option-0").locator("svg")).to_be_visible()
    expect(page.get_by_test_id("option-0").get_by_text(selected_country)).to_be_visible()
    page.get_by_test_id("structured-search-input-field-query").press("Enter")