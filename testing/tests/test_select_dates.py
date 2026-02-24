from playwright.sync_api import Page, expect
from datetime import date
import random

from testing.models import Result

TEST_ID = "test_select_dates"


def _save(test_case: str, url: str, passed: bool, comment: str = "") -> None:
    Result.objects.create(
        test_id=TEST_ID,
        test_case=test_case,
        url=url,
        passed=passed,
        comment=comment,
    )


def test_select_dates(page: Page) -> None:
    today = date.today()

    # Target: the 12th and 18th, 5 months from now
    months_ahead = random.randint(3, 8)  # Randomly choose between 3 to 8 months ahead to ensure we test the "Move forward" button
    raw_month = today.month + months_ahead
    target_year = today.year + (raw_month - 1) // 12
    target_month = ((raw_month - 1) % 12) + 1

    checkin = date(target_year, target_month, 12)
    checkout = date(target_year, target_month, 18)

    # Number of "Move forward" clicks to reach the target month
    clicks = (target_year - today.year) * 12 + (target_month - today.month)

    # Button names match Airbnb's aria labels, e.g. "12, Sunday, July 2026."
    checkin_name = f"{checkin.day}, {checkin.strftime('%A')}, {checkin.strftime('%B %Y')}."
    checkout_name = f"{checkout.day}, {checkout.strftime('%A')}, {checkout.strftime('%B %Y')}."

    # Expected text in search bar, e.g. "Jul 12 - 18"
    expected_text = f"{checkin.strftime('%b')} {checkin.day} - {checkout.day}"

    page.screenshot(path="screenshots/screenshot3.png")
    for _ in range(clicks):
        page.get_by_role("button", name="Move forward to switch to the").click()
        page.wait_for_timeout(1000)
    page.get_by_role("button", name=checkin_name).click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name=checkout_name).click()
    page.wait_for_timeout(1000)
    page.screenshot(path="screenshots/screenshot4.png")

    try:
        expect(page.get_by_role("search")).to_contain_text(expected_text)
        _save(f"Search bar shows selected dates: {expected_text}", page.url, True)
    except AssertionError as e:
        _save(f"Search bar shows selected dates: {expected_text}", page.url, False, str(e))

    return expected_text