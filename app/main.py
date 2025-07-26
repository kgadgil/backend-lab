from fastapi import FastAPI, HTTPException, Depends, Security
from pydantic import BaseModel
from sqlalchemy.orm import Session

## Auth
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError

## Local imports
from app.models import Base, engine, SessionLocal, NotaBene, User
from app.auth import hash_password, verify_password, create_access_token, decode_token

Base.metadata.create_all(bind=engine)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")


## PYDANTIC SCHEMAS
class UserCreate(BaseModel):
	username: str
	password: str

class NoteCreate(BaseModel):
	note: str

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

## AUTH
def get_current_user(
    token: str = Security(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        payload = decode_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token or expired")

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user


## ROUTES
## How do decorated functions work
## https://stackoverflow.com/questions/46123448/how-do-decorated-functions-work-in-flask-python-app-route
## decorator adds endpoint to app object declared above
## does the equivalent of calling the following function as follows
## app.add_url_rule("/", "notes", add_note)
## Decorators are functions that wrap other functions

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")
    hashed = hash_password(user.password)
    db_user = User(username=user.username, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    return {"message": "User registered"}

@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form.username).first()
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/notes")
def add_note(note: NoteCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
	db_note = NotaBene(username = current_user.username, note = note.note)
	db.add(db_note)
	db.commit()
	db.refresh(db_note)
	return {"message": "Note added successfully"}

@app.get("/notes/{username}")
def get_notes(username: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
	if username != current_user.username:
		raise HTTPException(status_code=403, detail="Not allowed")
	notes = db.query(NotaBene).filter(NotaBene.username == username).all()
	return {"username":username, "notes": [n.note for n in notes]}