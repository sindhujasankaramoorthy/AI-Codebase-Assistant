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
    total_size = 0
    extension_count = {}
    largest_file = None
    smallest_file = None
    average_file_size = 0
    most_common_extension = None
    summary = {
        "has_readme": False,
        "has_license": False,
        "has_gitignore": False,
        "main_language": None
    }

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
            relative_path = os.path.relpath(file_path, path)

            if file_name.upper().startswith("README"):
                summary["has_readme"] = True
            if file_name.upper().startswith("LICENSE"):
                summary["has_license"] = True
            if file_name == ".gitignore":
                summary["has_gitignore"] = True

            
            #largest file
            if largest_file is None:
                largest_file = {
                    "name": file_name,
                    "path": relative_path,
                    "size": file_size
                }
            elif file_size > largest_file["size"]:
                largest_file = {
                    "name": file_name,
                    "path": relative_path,
                    "size" :file_size
                }

            if smallest_file is None:
                smallest_file = {
                    "name": file_name,
                    "path": relative_path,
                    "size": file_size
                }
            elif file_size < smallest_file["size"]:
                smallest_file = {
                    "name": file_name,
                    "path": relative_path,
                    "size": file_size
                }
                                        
            
            #total size of files in repo
            total_size += file_size

            #count extension
            if file_extension in extension_count:
                extension_count[file_extension] += 1
            else:
                extension_count[file_extension] = 1

            #reading contents in file
            if file_extension in supported_extensions:
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                except Exception:
                    content = None
            else:
                content = None


            files.append({
                "name": file_name,
                "path": relative_path,
                "extension": file_extension,
                "size": file_size,
                "content": content
            })

    #average file size in repo
    if len(files) > 0:
        average_file_size = total_size / len(files)
    else:
        average_file_size = 0

    #finding most common extension in repo
    for extension, count in extension_count.items():
        if most_common_extension is None:
            most_common_extension = {
                "extension": extension,
                "count": count
            }
        elif count > most_common_extension["count"]:
            most_common_extension = {
                "extension": extension,
                "count": count
            }

            
    if most_common_extension:
         summary["main_language"] = most_common_extension["extension"]
    
    return {
        "total_files":  len(files),
        "total_size": total_size,
        "extension_count": extension_count,
        "largest_file": largest_file,
        "smallest_file":smallest_file,
        "average_file_size": average_file_size,
        "most_common_extension": most_common_extension,
        "summary": summary,
        "files": files
    }