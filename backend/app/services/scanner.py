import os

def scan_repository(path: str):
    files= []
    #directories can be reprsented as _ in python it is used to say unused variable
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            file_path=os.path.join(root,filename)
            files.append(file_path)
    
    return files