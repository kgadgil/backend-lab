# FastAPI Under Load: Scalable Web App with Authentication and Kubernetes

This project demonstrates the evolution of a simple FastAPI web application from local development using SQLite to a scalable, containerized microservice using PostgreSQL and Kubernetes. The project showcases key architectural decisions made to handle high-concurrency traffic and ensure robust authentication. 

## Quickstart

```
docker compose up --build
```

## Goal
- Build a simple, functional FastAPI app with user authentication to store user notes
- Containerize the app for reproducible environments
- Replace SQLite with PostgreSQL to handle traffic
- Deploy to Kubernetes to ensure scalability and fault tolerance
- Simulate real-world load
- Design decisions documented in ADRs under docs/
- Prototype -> Secure -> Scale -> Deploy -> Test -> Automate

## Design Decision Summary
- FastAPI used as a learning exercise. It's fast, async-native (will be used in the future) easy to setup RESTful APIs
- SQLite was used for prototyping the notes app. Doesn't support high traffic. 
- PostgreSQL better suited for handling simultaneous requests and larger deployments. 
- SQLAlchemy for ORM and Pydantic for data validation.
- Docker used for consistent environments across local/dev/prod

## Load Testing Results
- SQLite when bombarded with 10k requests crashes the Docker container with an SQLAlchemy connection timeout error. 
- TODO lots of user trying to register, login, add notes at once

## Keywords
FastAPI, SQLAlchemy, Pydantic, SQLite, PostgreSQL, Docker, Kubernetes