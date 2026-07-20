from fastapi import FastAPI
from app.services.scanner import scan_repository
from app.services.github import clone_repository
from app.services.chunker import create_chunks
from fastapi import Query

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to AI Codebase Assistant"}

@app.get("/scan")
def scan():
    return scan_repository(".")

@app.get("/scan-github")
def scan_github(url: str = Query(...)):
    repository_path = clone_repository(url)
    repository_data = scan_repository(repository_path)
    chunks = create_chunks(repository_data["files"])

    return {
        "repository_url": url,
        **repository_data,
        "chunks": chunks
    }