from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# In memory storage
db: Dict[str, List[str]] = {}

class Note(BaseModel):
	username:str
	note: str

## Test out Note model with external input
## $ python3 app/main.py 
## username='kgadgil' note='Hello World'
# external_input = {
# 	"username": "kgadgil",
# 	"note": "Hello World",
# }

# note = Note(**external_input)
# print(note)

## How do decorated functions work
## https://stackoverflow.com/questions/46123448/how-do-decorated-functions-work-in-flask-python-app-route
## decorator adds endpoint to app object declared above
## does the equivalent of calling the following function as follows
## app.add_url_rule("/", "notes", add_note)
## Decorators are functions that wrap other functions
@app.post("/notes")
def add_note(note: Note):
	if note.username not in db:
		db[note.username] = []
	db[note.username].append(note.note)
	return {"message": "Note added successfully"}

@app.get("/notes/{username}")
def get_notes(username: str):
	if username not in db:
		raise HTTPException(status_code=404, detail="User not found")
	return {"username":username, "notes": db[username]}

