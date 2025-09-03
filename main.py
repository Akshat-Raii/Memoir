from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates,templates 
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from bson.objectid import ObjectId


# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["notes"]
collection = db["notes"]





# Add note route
@app.post("/add-note", response_class=HTMLResponse)
async def add_note(request: Request, title: str = Form(...), content: str = Form(...)):
    collection.insert_one({"title": title, "content": content})
    notes = list(collection.find({}))
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes})
