from playwright.sync_api import Page, expect

from testing.models import Result

TEST_ID = "test_submit_search"


def _save(test_case: str, url: str, passed: bool, comment: str = "") -> None:
    Result.objects.create(
        test_id=TEST_ID,
        test_case=test_case,
        url=url,
        passed=passed,
        comment=comment,
    )


def test_submit_search(page: Page, selected_dates: str, guests: str) -> None:
    page.get_by_test_id("structured-search-input-search-button").click()
    page.wait_for_timeout(5000)
    if page.get_by_role("button", name="Got it").is_visible():
        page.get_by_role("button", name="Got it").click()
    page.screenshot(path="screenshots/screenshot7.png")

    date_text = selected_dates.replace("-", "\u2013")
    try:
        expect(page.get_by_test_id("little-search-date")).to_contain_text(date_text)
        _save(f"Search results show selected dates: {date_text}", page.url, True)
    except AssertionError as e:
        _save(f"Search results show selected dates: {date_text}", page.url, False, str(e))

    try:
        expect(page.get_by_test_id("little-search-guests")).to_contain_text(guests)
        _save(f"Search results show guest count: {guests}", page.url, True)
    except AssertionError as e:
        _save(f"Search results show guest count: {guests}", page.url, False, str(e))