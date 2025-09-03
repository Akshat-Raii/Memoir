def noteEntity(item) -> dict:
    return {
        "title": str(item["title"]),
        "content": item["content"]
    }
    

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items] 