from pydantic import BaseModel, Field


class Note(BaseModel):
    title : str
    content: str
    important: bool
    
    
    