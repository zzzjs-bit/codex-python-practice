import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_cli(*args):
    return subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "main.py"), *args],
        capture_output=True,
        text=True,
        check=False,
    )


def test_converts_jpy_to_cny():
    result = run_cli("--jpy", "10000", "--rate", "0.046")

    assert result.returncode == 0
    assert result.stdout.strip() == "10000 JPY ≈ 460.00 CNY"


def test_missing_parameters_show_usage():
    result = run_cli("--jpy", "10000")

    assert result.returncode != 0
    assert "usage:" in result.stderr.lower()
    assert "--rate" in result.stderr


def test_rejects_non_numeric_arguments():
    result = run_cli("--jpy", "abc", "--rate", "0.046")

    assert result.returncode != 0
    assert "--jpy must be a number" in result.stderr


def test_rejects_unreasonable_values():
    result = run_cli("--jpy", "-100", "--rate", "0.046")

    assert result.returncode != 0
    assert "--jpy must be greater than 0" in result.stderr
