# Airbnb E2E Testing

A Django-based end-to-end testing framework for [airbnb.com](https://www.airbnb.com) using [Playwright](https://playwright.dev/python/). Test results are persisted to a SQLite database and viewable through the Django admin interface.

## Features

- Automated browser tests against the live Airbnb website
- Test results (pass/fail, URL, comments) saved to a SQLite database
- Django admin interface for reviewing results
- Screenshots captured at key test steps

## Test Suite

The suite runs the following tests in sequence:

| Test            | File                      | Description                                                                                          |
| --------------- | ------------------------- | ---------------------------------------------------------------------------------------------------- |
| Search Location | `test_search_location.py` | Types a random country into the search bar and verifies the suggestions listbox and SVG icons appear |
| Select Dates    | `test_select_dates.py`    | Opens the date picker and selects random check-in/check-out dates                                    |
| Add Guests      | `test_add_guests.py`      | Increments the guest count and verifies the UI updates                                               |
| Submit Search   | `test_submit_search.py`   | Clicks the search button and verifies selected dates and guest count appear in results               |
| Item Details    | `test_item_details.py`    | Opens a random listing, verifies the h1 heading, site content, and collects image URLs               |

## Requirements

- Python 3.12+
- Google Chrome (used by Playwright)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mubashirul-Islam/airbnb-e2e-testing.git
   cd airbnb-e2e-testing
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**

   ```bash
   playwright install chromium
   ```

5. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

## Running the Tests

```bash
python manage.py runtest
```

This launches a visible Chromium browser, runs all five tests in sequence, and saves each result to the database. Screenshots are saved to the `screenshots/` directory.

## Viewing Results

Start the Django development server:

```bash
python manage.py runserver
```

Then open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and navigate to **Testing > Results**.

The admin panel supports filtering by `test_id` and `passed`, and searching by `test_id`, `test_case`, or `comment`.

## Project Structure

```
airbnb-e2e-testing/
├── config/                  # Django project settings and URLs
├── testing/
│   ├── models.py            # Result model (test_id, test_case, url, passed, comment)
│   ├── admin.py             # Django admin registration
│   ├── management/
│   │   └── commands/
│   │       └── runtest.py   # `python manage.py runtest` command
│   ├── migrations/          # Database migrations
│   └── tests/
│       ├── base.py          # Test runner entry point
│       ├── test_search_location.py
│       ├── test_select_dates.py
│       ├── test_add_guests.py
│       ├── test_submit_search.py
│       └── test_item_details.py
├── screenshots/             # Screenshots captured during test runs
├── db.sqlite3               # SQLite database
└── requirements.txt
```

## Result Model

Each test assertion is saved as a `Result` record:

| Field       | Type         | Description                                                  |
| ----------- | ------------ | ------------------------------------------------------------ |
| `test_id`   | CharField    | Identifier for the test module (e.g. `test_search_location`) |
| `test_case` | CharField    | Description of the specific assertion                        |
| `url`       | URLField     | Page URL at the time of the assertion                        |
| `passed`    | BooleanField | Whether the assertion passed                                 |
| `comment`   | TextField    | Error message or additional info                             |
