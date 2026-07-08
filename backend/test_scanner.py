from app.services.scanner import scan_repository

files = scan_repository(".")

for file in files:
    print(file)