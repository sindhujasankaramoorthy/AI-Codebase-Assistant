from app.services.scanner import scan_repository
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {
        "message":"Welcome to AI Codebase Assistant"
    }

@app.get("/scan")
def scan():
    files = scan_repository(".")
    return{
        "files":files
    }