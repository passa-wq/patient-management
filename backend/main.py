from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import Base, engine
from backend.routers import patients
import backend.models as models

app = FastAPI(
    title="Patient Management API",
    description="Ein Backend-Projekt zur Verwaltung von Patienten",
    version="1.0.0"
)

# CORS für Vue (Vite)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tabellen DB
Base.metadata.create_all(bind=engine)

# API Router
app.include_router(patients.router)


@app.get("/")
def root():
    return {"message": "Patient Management API läuft!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
