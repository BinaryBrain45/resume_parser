from fastapi import FastAPI, File, UploadFile, Depends
from sqlalchemy.orm import Session
import shutil
from backend.database import SessionLocal, Resume
from backend.resume_extractor import extract_text_from_pdf, extract_info
from backend.llm_analysis import analyze_resume

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = extract_text_from_pdf(file_path)
    info = extract_info(text)
    suggestions = analyze_resume(text)

    resume = Resume(
        name=info["name"],
        email=info["email"],
        phone=info["phone"],
        core_skills=["Python", "FastAPI"],  # Placeholder
        soft_skills=["Leadership", "Problem Solving"],
        experience=text[:200],
        resume_rating=8,
        improvement_areas=suggestions,
        upskill_suggestions="Learn React, Cloud Computing"
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return {"message": "Resume uploaded successfully", "data": resume}

@app.get("/get_resumes/")
def get_resumes(db: Session = Depends(get_db)):
    resumes = db.query(Resume).all()
    return resumes
