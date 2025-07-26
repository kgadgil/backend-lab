# 4. hot reload and sqlite in docker

Date: 2025-07-26

## Status

Accepted

## Context

To improve development experience, developer should be able to access the docker container and run sqlite3 to perform queries. The app should also hot reload when changes have been made so that developer doesn't have to keep running docker compose up everytime.

## Decision

* Add line to install sqlite in Dockerfile
* Add command to docker compose to run the server with reload option

## Consequences

Might introduce maintainence bugs when deployed. Will need to separate into prod and dev runs in the future when deployed.
