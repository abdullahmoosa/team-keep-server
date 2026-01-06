from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from supabase import create_client, Client
from dotenv import load_dotenv
import os

from routers import users, projects

load_dotenv()
app = FastAPI(
    title="Team Keep API",
    description="Backend API for Team Keep AI Engineering application",
    version="1.0.0"
)


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(projects.router)

# Health check endpoints
@app.get("/")
async def root():
    return {"message": "Team Keep AI app is running!"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0"
    }

