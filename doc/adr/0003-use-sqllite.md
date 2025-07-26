# 3. use sqllite

Date: 2025-07-26

## Status

Accepted

## Context

For persistent note storage, we will use SQLLite.

## Decision

* Use SQLAlchemy to handle ORM (Object Relational Mapper)
* SQLLite as database. Simple file based DB

## Consequences

Will be able to start database and app as separate services in the future with the goal of deploying on Kubernetes