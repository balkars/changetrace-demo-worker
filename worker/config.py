import os

# Delay before retrying a failed job, in seconds.
RETRY_DELAY_SECONDS = int(os.getenv("RETRY_DELAY_SECONDS", 0))
# Exponential backoff applied from the second retry onward, in seconds.
RETRY_BACKOFF_BASE_SECONDS = int(os.getenv("RETRY_BACKOFF_BASE_SECONDS", 1))
RETRY_BACKOFF_MAX_SECONDS = int(os.getenv("RETRY_BACKOFF_MAX_SECONDS", 30))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 5))
