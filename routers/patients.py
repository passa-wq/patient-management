from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from pydantic import BaseModel
from datetime import date

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)

class PatientCreate(BaseModel):
    vorname: str
    nachname: str
    geburtsdatum: date | None = None
    email: str | None = None
    telefon: str | None = None
    krankengeschichte: str | None = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET /patients 
@router.get("/")
def get_patients(db: Session = Depends(get_db)):
    patients = db.query(models.Patient).all()
    return patients

# POST /patients — Neue Patient hinzufügen
@router.post("/")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = models.Patient(
        vorname=patient.vorname,
        nachname=patient.nachname,
        geburtsdatum=patient.geburtsdatum,
        email=patient.email,
        telefon=patient.telefon,
        krankengeschichte=patient.krankengeschichte
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient
