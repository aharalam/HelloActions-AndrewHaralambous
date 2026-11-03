"""Check the real script with and without its environment variable."""

import os
from pathlib import Path
import subprocess
import sys
import unittest


class HelloTests(unittest.TestCase):
    def test_greets_the_name_from_the_environment(self):
        environment = os.environ.copy()
        environment["WHO_TO_GREET"] = "Andrew Haralambous"
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("hello.py"))],
            env=environment, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), [
            "Hello Andrew Haralambous!",
            "This program is running inside GitHub Actions.",
        ])

    def test_uses_the_default_when_the_variable_is_missing(self):
        environment = os.environ.copy()
        environment.pop("WHO_TO_GREET", None)
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("hello.py"))],
            env=environment, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), [
            "Hello GitHub Actions Student!",
            "This program is running inside GitHub Actions.",
        ])


if __name__ == "__main__":
    unittest.main()
