import os

def scan_repository(path: str):
    ignored_directories = {
        ".git",
        ".venv",
        "venv",
        "node_modules",
        "__pycache__"
    }

    supported_extensions = {
        ".py",
        ".java",
        ".js",
        ".ts",
        ".html",
        ".css",
        ".md",
        ".txt",
        ".json",
        ".yml",
        ".yaml"
    }

    files= []
    #directories can be reprsented as _ in python it is used to say unused variable
    for root, directories, filenames in os.walk(path):
        directories[:] = [
            directory
            for directory in directories
            if directory not in ignored_directories
        ]

        for filename in filenames:
            file_path=os.path.join(root,filename)
            file_name = os.path.basename(file_path)
            file_extension = os.path.splitext(file_path)[1]
            file_size = os.path.getsize(file_path)

            if file_extension in supported_extensions:
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                except Exception:
                    content = None
            else:
                content = None
                
            relative_path = os.path.relpath(file_path,path)

            files.append({
                "name": file_name,
                "path": relative_path,
                "extension": file_extension,
                "size": file_size,
                "content": content
            })
    
    return files