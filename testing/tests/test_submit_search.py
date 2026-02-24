from playwright.sync_api import Page, expect


def test_submit_search(page: Page, selected_dates: str, guests: str) -> None:
    page.get_by_test_id("structured-search-input-search-button").click()
    page.wait_for_timeout(5000)
    if page.get_by_role("button", name="Got it").is_visible():
        page.get_by_role("button", name="Got it").click()
    page.screenshot(path="screenshots/screenshot7.png")    
    expect(page.get_by_test_id("little-search-date")).to_contain_text(selected_dates.replace("-", "–"))
    expect(page.get_by_test_id("little-search-guests")).to_contain_text(guests)