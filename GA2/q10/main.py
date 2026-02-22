import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Deployment Observability API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "status": "healthy",
        "service": "deployment-ready-ga2-70fd93",
        "port": int(os.environ.get("APP_PORT", 7006)),
    }


@app.get("/health")
async def health():
    return {"status": "ok"}