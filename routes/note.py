from fastapi import APIRouter
from models.note import Note
from fastapi import Form
from config.db import collection
from schemas.note import noteEntity, notesEntity
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates


note = APIRouter()
templates = Jinja2Templates(directory="templates")


# Home route
@note.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    notes = list(collection.find({}))
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes})



@note.post("/add-note", response_class=HTMLResponse)
async def create_note(request: Request, title: str = Form(...), content: str = Form(...)):
    note = {"title": title, "content": content}
    collection.insert_one(note)
    notes = list(collection.find({}))
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes})


# Get all notes as JSON
@note.get("/api/notes")
async def get_notes():
    notes = list(collection.find({}))
    return {"notes": notesEntity(notes)}

# Get single note by id
@note.get("/api/notes/{note_id}")
async def get_note(note_id: str):
    note = collection.find_one({"_id": note_id})
    if not note:
        return JSONResponse(status_code=404, content={"message": "Note not found"})
    return noteEntity(note)

# Create note using JSON
@note.post("/api/notes")
async def create_note_api(note: Note):
    result = collection.insert_one(note.dict())
    return {"id": str(result.inserted_id), "message": "Note added successfully"}