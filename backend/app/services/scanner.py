import os

def scan_repository(path: str):
    ignored_directories = {
        ".git",
        ".venv",
        "venv",
        "node_modules",
        "__pycache__"
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

            files.append({
                "name": file_name,
                "path": file_path,
                "extension": file_extension,
                "size": file_size
            })
    
    return files