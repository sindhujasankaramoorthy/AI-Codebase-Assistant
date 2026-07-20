def chunk_text(text, chunk_size=5000, overlap=500):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks



def create_chunks(files):
    all_chunks = []
    
    for file in files:
        content = file["content"]

        if content is None:
            continue

        chunks = chunk_text(content)

        for index, chunk in enumerate(chunks):
            all_chunks.append({
               "file_name": file["name"],
                "path": file["path"],
                "extension": file["extension"],
                "chunk_id": index,
                "content": chunk
            })

    return all_chunks




