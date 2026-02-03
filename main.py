from fastapi import FastAPI
from database import Base, engine
import models
from routers import patients

app = FastAPI(
    title="Patient Management API",
    description="Ein Backend-Projekt zur Verwaltung von Patienten",
    version="1.0.0"
)

# Tabellen in der Datenbank erstellen
Base.metadata.create_all(bind=engine)

# Router hinzufügen
app.include_router(patients.router)

@app.get("/")
def read_root():
    return {"message": "Patient Management API läuft!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
