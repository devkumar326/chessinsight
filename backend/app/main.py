from fastapi import FastAPI
from app.api.v1.health import router as health_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ChessInsight API", version="1.0")
# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "ChessInsight backend running"}
