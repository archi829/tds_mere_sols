# FastAPI — Practical Guide & Decision README

## What is FastAPI and why would I use it?

FastAPI is a modern, high‑performance Python web framework for building APIs with minimal code. It leverages Python type hints for automatic data validation, generates interactive OpenAPI documentation (Swagger & ReDoc), and supports async operations for superior performance in I/O‑heavy applications like microservices and ML inference APIs.

You would typically choose FastAPI over traditional frameworks like Flask when you need:

* Rapid API development with less boilerplate
* Automatic request/response validation
* Interactive documentation out‑of‑the‑box
* High concurrency and scalability
* Built‑in OAuth2/auth support

### Key Benefits

**Performance**
Async‑native (Starlette + Uvicorn). Handles very high throughput (15k+ RPS in benchmarks), often far exceeding Flask.

**Developer Experience**
Type‑safe design, automatic validation, and generated docs reduce bugs and onboarding time.

**Typical Use Cases**

* REST APIs & microservices
* ML model serving / inference endpoints
* Real‑time apps (WebSockets / SSE)
* IoT backends
* Vector DB / AI services

---

## Popular, Modern Alternatives

| Framework              | Best For                | Performance | Learning Curve | Docs / Validation |
| ---------------------- | ----------------------- | ----------- | -------------- | ----------------- |
| **FastAPI**            | APIs, async, ML         | ⭐ Highest   | Low            | ⭐ Excellent       |
| **Flask**              | Simple apps, prototypes | Medium      | ⭐ Lowest       | Manual            |
| **Litestar**           | Complex async systems   | High        | Medium         | Strong            |
| **Sanic**              | Raw async speed         | Very High   | Medium         | Good              |
| **Django + DRF/Ninja** | Full web apps + APIs    | Medium      | Higher         | Strong            |

### Alternative Notes

* **Flask** → Minimalist, huge ecosystem, synchronous by default
* **Litestar** → Structured successor to Starlette with DI & modular design
* **Sanic** → Extremely fast async server, fewer batteries included
* **Django Ninja** → FastAPI‑like layer on Django

---

## Decision Tree — What should I use?

**Need full web app (templates, admin, ORM)?**
→ Django

**Simple prototype or low‑traffic API?**
→ Flask

**API‑focused project?**

* Need high concurrency / async (ML, microservices)? → **FastAPI**
* Need extreme raw speed, minimal features? → **Sanic**
* Want Starlette‑style but more structure? → **Litestar**
* Already using Django? → **Django Ninja**

👉 For AI/ML APIs (model serving, vector DB, embeddings): **FastAPI is usually the best choice.**

---

# ✨ “Magical” FastAPI Features (with Examples)

FastAPI feels powerful because Python type hints drive validation, docs, and dependency injection automatically.

---

## 1. Automatic Interactive API Documentation

FastAPI auto‑generates Swagger & ReDoc from your code.

Run app → open:

* `/docs`
* `/redoc`

### Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

This automatically produces:

* Parameter UI
* Schema
* Try‑it‑out button
* Response model

No YAML or manual docs needed.

---

## 2. Automatic Data Validation (Pydantic)

Request bodies are validated automatically using Python types.

### Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

If invalid JSON is sent → FastAPI returns structured 422 errors automatically.

No manual validation code required.

---

## 3. Dependency Injection (Clean & Reusable)

Dependencies are declared once and injected automatically.

### Example — Auth dependency

```python
from fastapi import FastAPI, Depends

app = FastAPI()

async def get_current_user(token: str):
    return {"user": "archita"}

@app.get("/users/me")
async def read_users_me(current_user = Depends(get_current_user)):
    return current_user
```

Features:

* Auto‑validation
* Caching per request
* Nested dependencies
* Test overrides

---

## 4. Async by Default (High Concurrency)

FastAPI uses ASGI and async/await for massive concurrency.

### Example

```python
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/async-data")
async def fetch_data():
    await asyncio.sleep(1)
    return {"data": "loaded"}
```

Handles thousands of concurrent I/O requests efficiently.

Perfect for:

* ML inference
* External APIs
* DB queries
* Streaming

---

# CORS in FastAPI

## What is CORS?

CORS (Cross‑Origin Resource Sharing) is a browser security mechanism that controls whether a web page from one origin can access resources from another origin.

It uses HTTP headers like:

* `Access-Control-Allow-Origin`
* `Access-Control-Allow-Methods`
* `Access-Control-Allow-Headers`

Without CORS, browsers block frontend → backend requests across domains/ports.

---

## Enable CORS in FastAPI

FastAPI provides `CORSMiddleware`.

### Basic Example (allow all — dev only)

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}
```

---

## Production‑Safe CORS Configuration

Never use `"*"` with credentials.

### Secure Example

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourfrontend.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)
```

---

## CORS Parameters Explained

| Parameter         | Purpose         | Example               |
| ----------------- | --------------- | --------------------- |
| allow_origins     | Allowed domains | `["https://app.com"]` |
| allow_methods     | HTTP methods    | `["GET","POST"]`      |
| allow_headers     | Custom headers  | `["Authorization"]`   |
| allow_credentials | Cookies/Auth    | `True`                |

---

## Common CORS Pitfalls

* Using `*` with credentials=True
* Port mismatch (3000 vs 8000)
* HTTP vs HTTPS mismatch
* Missing Authorization header in allow_headers
* Forgetting OPTIONS preflight

FastAPI middleware handles preflight automatically.

---

# Summary — When to Choose FastAPI

Choose **FastAPI** if you want:

* High‑performance APIs
* Async concurrency
* ML inference endpoints
* Automatic validation
* Interactive docs
* Clean dependency injection

Avoid FastAPI if you need:

* Full CMS/admin → Django
* Ultra‑simple scripts → Flask

---

# Quick Start

Install:

```bash
pip install fastapi uvicorn
```

Run:

```bash
uvicorn main:app --reload
```

Open docs:

```
http://127.0.0.1:8000/docs
```

---

# Final Takeaway

FastAPI combines the speed of Node/Go frameworks with Python’s simplicity and type safety, making it the current best choice for modern APIs, especially in AI/ML systems and scalable microservices architectures.
