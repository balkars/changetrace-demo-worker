import os

# Delay before retrying a failed job, in seconds.
RETRY_DELAY_SECONDS = int(os.getenv("RETRY_DELAY_SECONDS", 2))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 5))
