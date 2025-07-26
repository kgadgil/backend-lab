from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# In memory storage
db: Dict[str, List[str]] = {}

class Note(BaseModel):
	username:str
	note: str

external_input = {
	"username": "kgadgil",
	"note": "Hello World",
}

note = Note(**external_input)
print(note)