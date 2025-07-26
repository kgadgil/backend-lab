from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

## Local imports
from app.models import Base, engine, SessionLocal, Note

Base.metadata.create_all(bind=engine)

app = FastAPI()

class NoteCreate(BaseModel):
	username:str
	note: str

	def __repr__(self):
	    return f"<Note(id={self.id}, username='{self.username}', note='{self.note[:20]}')>"

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

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
def add_note(note: NoteCreate, db: Session = Depends(get_db)):
	db_note = Note(username = note.username, note = note.note)
	db.add(db_note)
	db.commit()
	db.refresh(db_note)
	return {"message": "Note added successfully", "id": db_note.id}

@app.get("/notes/{username}")
def get_notes(username: str, db: Session = Depends(get_db)):
	notes = db.query(Note).filter(Note.username == username).all()
	if not notes: 
		raise HTTPException(status_code=404, detail="User not found")
	return {"username":username, "notes": [n.note for n in notes]}

