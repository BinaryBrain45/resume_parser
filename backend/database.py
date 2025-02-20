from sqlalchemy import create_engine, Column, Integer, String, Text, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://fuzzie_user:password@localhost/resume_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    core_skills = Column(ARRAY(String))
    soft_skills = Column(ARRAY(String))
    experience = Column(Text)
    resume_rating = Column(Integer)
    improvement_areas = Column(Text)
    upskill_suggestions = Column(Text)

def init_db():
    Base.metadata.create_all(bind=engine)
