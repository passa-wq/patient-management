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


class PatientUpdate(BaseModel):
    vorname: str | None = None
    nachname: str | None = None
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

# GET /patients/{patient_id}
@router.get("/{patient_id}")
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient nicht gefunden")
    return patient

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

# PUT /patients/{patient_id}
@router.put("/{patient_id}")
def update_patient(
    patient_id: int,
    patient_update: PatientUpdate,
    db: Session = Depends(get_db)
):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient nicht gefunden")

    for key, value in patient_update.dict(exclude_unset=True).items():
        setattr(patient, key, value)

    db.commit()
    db.refresh(patient)
    return patient

# DELETE /patients/{patient_id}
@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient nicht gefunden")

    db.delete(patient)
    db.commit()
    return {"detail": "Patient erfolgreich gelöscht"}