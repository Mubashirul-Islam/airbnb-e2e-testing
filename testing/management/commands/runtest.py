import subprocess
import sys
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run Playwright e2e tests in testing/tests/base.py"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Running Playwright tests..."))

        result = subprocess.run(
            [sys.executable, "-m", "testing.tests.base"],
            capture_output=False,
        )

        if result.returncode == 0:
            self.stdout.write(self.style.SUCCESS("Tests passed successfully."))
        else:
            self.stderr.write(self.style.ERROR(f"Tests failed with exit code {result.returncode}."))
            sys.exit(result.returncode)
