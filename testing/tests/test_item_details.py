import random
from playwright.sync_api import Page, expect

from testing.models import Result

TEST_ID = "test_item_details"


def _save(test_case: str, url: str, passed: bool, comment: str = "") -> None:
    Result.objects.create(
        test_id=TEST_ID,
        test_case=test_case,
        url=url,
        passed=passed,
        comment=comment,
    )


def test_item_details(page: Page) -> None:
    item_sl = random.randint(1, 18)
    with page.expect_popup() as page1_info:
        page.locator(f"div:nth-child({item_sl}) > .cfutgp0 > div > div > div > .cy5jw6o > .lxq01kf > .mz543g6 > .c14dgvke > .cnjlbcx > .s1yvqyx7 > div > .awuxh4x > .cw9aemg > .c14whb16 > a").first.click()
    page1 = page1_info.value
    page1.wait_for_timeout(1000)
    if page1.get_by_text("Translation onThis symbol").is_visible():
        page1.screenshot(path="screenshots/screenshot8.png")
        page1.get_by_role("button", name="Close").click()
    page1.screenshot(path="screenshots/screenshot9.png")

    try:
        title = page1.locator("h1").inner_text()
        expect(page1.locator("h1")).to_be_visible()
        _save(f"Item details page has visible h1 heading: {title}", page1.url, True)
    except AssertionError as e:
        _save("Item details page has visible h1 heading", page1.url, False, str(e))

    try:
        subtitle = page1.locator("#site-content").inner_text()
        expect(page1.locator("#site-content")).to_be_visible()
        _save(f"Item details page has visible site content with subtitle: {subtitle}", page1.url, True)
    except AssertionError as e:
        _save("Item details page has visible site content", page1.url, False, str(e))

    imgs = page.locator("img[data-original-uri]")
    count = imgs.count()

    image_urls = []
    for i in range(count):
        url = imgs.nth(i).get_attribute("data-original-uri")
        image_urls.append(url)

    _save(
        f"Item details page has {count} images",
        page1.url,
        count > 0,
        comment="\n".join(filter(None, image_urls)),
    )    