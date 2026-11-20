from __future__ import annotations

import sys

from worker import config


def retry_delay(attempt: int = 1) -> int:
    """Seconds to wait before retry number `attempt` (1-based) of a failed job.

    The first retry uses RETRY_DELAY_SECONDS (0 by default, see CTX-001); later
    retries back off exponentially, capped at RETRY_BACKOFF_MAX_SECONDS.
    """
    if attempt <= 1:
        return config.RETRY_DELAY_SECONDS
    backoff = config.RETRY_BACKOFF_BASE_SECONDS * 2 ** (attempt - 2)
    return min(backoff, config.RETRY_BACKOFF_MAX_SECONDS)


if __name__ == "__main__":
    if "--smoke" in sys.argv[1:]:
        print(f"retry delay: {retry_delay()}s")
        sys.exit(0)
    print("usage: python -m worker.retry --smoke", file=sys.stderr)
    sys.exit(2)
