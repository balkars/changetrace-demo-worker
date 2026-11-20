---
id: CTX-002
kind: decision
title: Bounded exponential backoff after first immediate retry
status: active
author: Dev B
created: '2026-11-20'
touches: [worker/config.py#RETRY_BACKOFF_BASE_SECONDS, worker/config.py#RETRY_BACKOFF_MAX_SECONDS]
guards:
- {file: worker/config.py, key: RETRY_BACKOFF_BASE_SECONDS, expect: '1', previous: null}
- {file: worker/config.py, key: RETRY_BACKOFF_MAX_SECONDS, expect: '30', previous: null}
supersedes: []
superseded_by: null
tags: []
---

## Problem
Immediate retries (CTX-001) can hammer a failing downstream such as the payments API.

## Decided
Keep the first retry immediate. From the second retry, back off exponentially (base 1s, doubling), capped at 30s. Base and cap are env-configurable.

## Tried and ruled out
Resetting RETRY_DELAY_SECONDS to 2: it undoes CTX-001 and slows every first retry.

## Assumptions
Most failures are transient and recover on the first immediate retry.

## Watch out
Setting the cap too high stalls job recovery. Setting the base to 0 disables backoff.

## Evidence
OBS-001 (request burst on dev); tests/test_retry.py backoff test.
