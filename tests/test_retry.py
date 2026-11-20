import subprocess
import sys
from pathlib import Path

from worker.config import RETRY_DELAY_SECONDS
from worker.retry import retry_delay

ROOT = Path(__file__).resolve().parent.parent


def test_recovers_without_delay():
    assert retry_delay() == RETRY_DELAY_SECONDS


def test_smoke_prints_delay():
    result = subprocess.run([sys.executable, "-m", "worker.retry", "--smoke"],
                            cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == f"retry delay: {RETRY_DELAY_SECONDS}s"
