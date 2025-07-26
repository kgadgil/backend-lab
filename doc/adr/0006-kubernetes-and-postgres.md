# 6. Kubernetes and Postgres

Date: 2025-07-26

## Status

Accepted

## Context

App fails under high load (10k requests). sqlite and single container setup are not enough for real-world scaling. 

## Decision

* Need orchestration and robust DB - use Kubernetes and PostgreSQL

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
