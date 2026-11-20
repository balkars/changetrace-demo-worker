---
id: CTX-001
kind: decision
title: Retry failed jobs immediately by default
status: active
author: Dev A
created: '2026-11-20'
touches: [worker/config.py#RETRY_DELAY_SECONDS]
guards:
- {file: worker/config.py, key: RETRY_DELAY_SECONDS, expect: '0', previous: '2'}
supersedes: []
superseded_by: null
tags: []
---

## Problem
Failed jobs waited 2 seconds (the `RETRY_DELAY_SECONDS` default) before each retry, up to 5 retries. This made recovery slow.

## Decided
Default `RETRY_DELAY_SECONDS` to 0 so failed jobs retry immediately. The value can still be set through the environment variable.

## Tried and ruled out
Keeping the 2s default: this is the slow recovery we are fixing.
Not yet tried: a short delay or exponential backoff, which would keep recovery fast while softening bursts.

## Assumptions
Most failures are transient and recover on a quick retry.
The `test_recovers_without_delay` test reflects the intended behaviour.

## Watch out
Immediate retries can burst against a downstream service that is down. With up to 5 retries per job, many failing jobs can hammer it and slow its recovery. If that happens, set `RETRY_DELAY_SECONDS` above 0 or add backoff.

## Evidence
`python -m pytest -q`: 2 passed.
`ct check --file worker/config.py`: no conflicts.
