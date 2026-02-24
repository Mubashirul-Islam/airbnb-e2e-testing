from playwright.sync_api import Page, expect


def test_item_details(page: Page) -> None:
    with page.expect_popup() as page1_info:
        page.locator("div:nth-child(2) > .cfutgp0 > div > div > div > .cy5jw6o > .lxq01kf > .mz543g6 > .c14dgvke > .cnjlbcx > .s1yvqyx7 > div > .awuxh4x > .cw9aemg > .c14whb16 > a").first.click()
    page1 = page1_info.value
    page1.wait_for_timeout(1000)
    if page1.get_by_text("Translation onThis symbol").is_visible():
        page1.screenshot(path="screenshots/screenshot8.png")
        page1.get_by_role("button", name="Close").click()
    page1.screenshot(path="screenshots/screenshot9.png")    
    expect(page1.locator("h1")).to_be_visible()
    expect(page1.locator("#site-content")).to_be_visible()