from backend.database import Base
from sqlalchemy import Column, Integer, String, Date

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    vorname = Column(String, nullable=False)
    nachname = Column(String, nullable=False)
    geburtsdatum = Column(Date, nullable=True)
    email = Column(String, unique=True, nullable=True)
    telefon = Column(String, nullable=True)
    krankengeschichte = Column(String, nullable=True)
