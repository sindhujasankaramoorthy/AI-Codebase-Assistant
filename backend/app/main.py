from fastapi import FastAPI
from app.services.scanner import scan_repository
from app.services.github import clone_repository
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
    files = scan_repository(repository_path)

    return {
        "repository_url": url,
        "total_files": len(files),
        "files": files
    }