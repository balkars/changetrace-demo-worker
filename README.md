# Worker service

A small job worker used to demonstrate ChangeTrace. `worker/config.py` holds the
retry settings; `worker/retry.py` reads them.

    python -m pytest -q
    python -m worker.retry --smoke

Decision records live in `.context/decisions/`. Run `ct explain worker/config.py`
before changing a setting, and `ct check` before opening a pull request.
