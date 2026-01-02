# API Gateway with Configurable Rate Limiting

## Overview

This project is a **production-grade API Gateway** built using **FastAPI**, designed to demonstrate real-world backend engineering concepts commonly used at FAANG-scale systems.

The gateway authenticates incoming requests using API keys stored in MongoDB and enforces **configurable rate limiting** strategies on a per-user basis using classic algorithms such as **Token Bucket** and **Sliding Window**.

The system is fully config-driven, extensible, and designed using clean OOP principles.

---

## Architecture

![API Gateway Architecture](/Api_gateway_architecture.png)

```
Client
  |
  |  (HTTP Request + API Key)
  v
FastAPI Gateway
  |
  |--> Auth Service (MongoDB)
  |--> RateLimiterFactory
          |--> Token Bucket Limiter
          |--> Sliding Window Limiter
  |--> Metrics Collector
  |
  v
Response (200 / 401 / 429)
```

---

## Key Features

* API-key based authentication
* MongoDB-backed user configuration
* Factory Pattern for dynamic rate limiter selection
* Strategy Pattern for rate limiting algorithms
* Per-user rate limiting
* Proper HTTP semantics (401, 429)
* Extensible backend design

---

## Tech Stack

* **Python 3.10**
* **FastAPI** – API Gateway
* **MongoDB** – Configuration & authentication store
* **Uvicorn** – ASGI server
* **Git** – Version control

---

## Rate Limiting Algorithms

### Token Bucket

* Allows bursts up to a defined capacity
* Tokens refill at a constant rate
* Commonly used in real-world APIs

### Sliding Window

* Tracks request count over a rolling time window
* Prevents request spikes

Each user can be assigned a different algorithm via MongoDB configuration.

---

## How to Run

### 1. Start MongoDB

```bash
sudo systemctl start mongod
```

### 2. Insert Test User

```bash
mongosh
use api_gateway

db.users.insertOne({
  user_id: "user_1",
  api_key: "valid-key",
  type: "token_bucket",
  capacity: 5,
  refill_rate: 1
})
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Server

```bash
uvicorn main:app --reload
```

---

## Testing

### Valid Request

```bash
curl -H "x-api-key: valid-key" http://127.0.0.1:8000/api
```

Response:

```json
{"status": "success"}
```

### Unauthorized Request

```bash
curl -H "x-api-key: wrong-key" http://127.0.0.1:8000/api
```

Response (401):

```json
{"error": "Unauthorized"}
```

### Rate Limit Exceeded

```bash
curl -H "x-api-key: valid-key" http://127.0.0.1:8000/api
```

Response (429):

```json
{"error": "Rate limit exceeded"}
```

---

## Design Highlights

* Clear separation of concerns
* Config-driven behavior (no hardcoded limits)
* Easily extensible for Redis / distributed rate limiting
* Production-style error handling

---

## Future Improvements

* Redis-backed distributed rate limiting
* Async MongoDB driver
* OpenAPI authentication documentation
* Load testing and benchmarking

---

## Author

Nimit Jindal
