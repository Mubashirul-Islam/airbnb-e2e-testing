from playwright.sync_api import Page, expect
import random

from testing.models import Result

TEST_ID = "test_search_location"


def _save(test_case: str, url: str, passed: bool, comment: str = "") -> None:
    Result.objects.create(
        test_id=TEST_ID,
        test_case=test_case,
        url=url,
        passed=passed,
        comment=comment,
    )


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

    try:
        expect(page.get_by_role("listbox", name="Search suggestions")).to_be_visible()
        _save("Search suggestions listbox is visible", page.url, True)
    except AssertionError as e:
        _save("Search suggestions listbox is visible", page.url, False, str(e))

    try:
        expect(page.get_by_test_id("option-0").locator("svg")).to_be_visible()
        _save("First suggestion option has SVG icon", page.url, True)
    except AssertionError as e:
        _save("First suggestion option has SVG icon", page.url, False, str(e))

    try:
        expect(page.get_by_test_id("option-0").get_by_text(selected_country)).to_be_visible()
        _save(f"First suggestion shows selected country: {selected_country}", page.url, True)
    except AssertionError as e:
        _save(f"First suggestion shows selected country: {selected_country}", page.url, False, str(e))

    page.get_by_test_id("structured-search-input-field-query").press("Enter")