from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./notes.db"

## https://docs.sqlalchemy.org/en/14/orm/quickstart.html
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Note(Base):
	__tablename__ = "notes"

	## All ORM mapped classes require at least one column be declared as part of the primary key
	id = Column(Integer, primary_key=True)
	## column is indexed. **more notes in DEV_HELPER
	username = Column(String, index=True)
	note = Column(String)