from fastapi import FastAPI
from database import Base, engine
import models  

# Tabellen erstellen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Patient Management API",
    description="Ein Backend-Projekt zur Verwaltung von Patienten",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Patient Management API läuft!"}
