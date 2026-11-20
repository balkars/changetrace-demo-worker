from __future__ import annotations

import sys

from worker import config


def retry_delay() -> int:
    """Seconds to wait before retrying a failed job."""
    return config.RETRY_DELAY_SECONDS


if __name__ == "__main__":
    if "--smoke" in sys.argv[1:]:
        print(f"retry delay: {retry_delay()}s")
        sys.exit(0)
    print("usage: python -m worker.retry --smoke", file=sys.stderr)
    sys.exit(2)
