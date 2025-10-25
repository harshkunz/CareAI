import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.route import router as text_router

from dotenv import load_dotenv

app = FastAPI(
    title="CareAI",
    description="",
    version="1.0.0"
)

frontend_url = os.getenv("FRONTEND_URL")
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

if frontend_url:
    origins.append(frontend_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(text_router, prefix="/input", tags=[""])


@app.get("/")
def root():
    return {"message": "Server is running!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)