from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routers import models
from app.config.settings import Settings

app = FastAPI(
    title="Satellite Image Classification API",
    description="API for satellite image classification using ML models",
    version="0.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(models.router, prefix="/api/v1", tags=["models"])

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}
