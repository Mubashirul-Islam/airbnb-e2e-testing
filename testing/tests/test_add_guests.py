import random
from playwright.sync_api import Page, expect

from testing.models import Result

TEST_ID = "test_add_guests"


def _save(test_case: str, url: str, passed: bool, comment: str = "") -> None:
    Result.objects.create(
        test_id=TEST_ID,
        test_case=test_case,
        url=url,
        passed=passed,
        comment=comment,
    )


def test_add_guests(page: Page) -> None:
    page.get_by_role("button", name="Who Add guests").click()

    try:
        expect(page.locator(".p1tlhulc")).to_be_visible()
        _save("Guests panel is visible after clicking 'Add guests'", page.url, True)
    except AssertionError as e:
        _save("Guests panel is visible after clicking 'Add guests'", page.url, False, str(e))
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

    expected_guests = f"{adults + children} guests, 1 infant, 1 pet"
    try:
        expect(page.get_by_role("search")).to_contain_text(expected_guests)
        _save(f"Search bar shows guest count: {expected_guests}", page.url, True)
    except AssertionError as e:
        _save(f"Search bar shows guest count: {expected_guests}", page.url, False, str(e))

    return f"{adults + children} guests"