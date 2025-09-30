from typing import Dict, Any
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Routers
from api.health import router as health_router

load_dotenv()

APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./complicopilot.db")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

app = FastAPI(title="CompliCopilot API", version=APP_VERSION)

# CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001", 
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
        "http://127.0.0.1:5500",
        "http://127.0.0.1:5501",
        "http://localhost:5500",
        "http://localhost:5501",
        "http://127.0.0.1:8000",
        "http://localhost:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach config
app.state.settings = {
    "DATABASE_URL": DATABASE_URL,
    "UPLOAD_DIR": UPLOAD_DIR,
    "LOG_LEVEL": LOG_LEVEL,
    "VERSION": APP_VERSION,
}

@app.get("/", tags=["root"])
def root() -> Dict[str, Any]:
    return {
        "message": "CompliCopilot API is running!",
        "status": "ok", 
        "service": "backend", 
        "version": APP_VERSION,
        "docs": "/docs",
        "endpoints": {
            "health": "/api/v1/health",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    }

# Include health router
app.include_router(health_router)