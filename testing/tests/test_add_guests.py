import random
from playwright.sync_api import Page, expect


def test_add_guests(page: Page) -> None:
    page.get_by_role("button", name="Who Add guests").click()
    expect(page.locator(".p1tlhulc")).to_be_visible()
    page.wait_for_timeout(1000)
    page.screenshot(path="screenshots/screenshot5.png")
    adults = random.randint(1, 3)
    children = random.randint(1, 3)
    for _ in range(adults):
        page.get_by_test_id("stepper-adults-increase-button").click()
        page.wait_for_timeout(1000)
    for _ in range(children):
        page.get_by_test_id("stepper-children-increase-button").click()
        page.wait_for_timeout(1000)
    page.get_by_test_id("stepper-infants-increase-button").click()
    page.wait_for_timeout(1000)
    page.get_by_test_id("stepper-pets-increase-button").click()
    page.screenshot(path="screenshots/screenshot6.png")
    expect(page.get_by_role("search")).to_contain_text(f"{adults + children} guests, 1 infant, 1 pet")
    return f"{adults + children} guests"