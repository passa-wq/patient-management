# patient-management

Dieses Backend-Projekt dient zur Verwaltung von Patienten.

## Funktionalität:
- Hinzufügen eines neuen Patienten
- Anzeigen der Patientenliste
- (Optional) Bearbeiten und Löschen von Patienten

## Technologien:
- FastAPI (REST API)
- SQL (Sqlite3)
- Python
- ERD-Diagramm mit Mermaid

## Installation:
1. Repository klonen:

    git clone https://github.com/<username>/patient-management-api.git
    cd patient-management-api

2. Virtuelle Umgebung erstellen (optional):
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate

3. Abhängigkeiten installieren:
    pip install fastapi uvicorn sqlalchemy

4. Projekt starten
    uvicorn main:app --reload

Die API ist danach erreichbar unter:
    http://127.0.0.1:8000

FastAPI stellt automatisch eine API-Dokumentation bereit:
    http://127.0.0.1:8000/docs
    

## Projektstruktur

```text
patient-management/
│
├── main.py              # Einstiegspunkt der Anwendung
├── database.py          # Datenbankverbindung
├── models.py            # SQLAlchemy Modelle
├── routers/
│   └── patients.py      # Patient-Routen (CRUD)
├── requirements.txt     # Abhängigkeiten
└── README.md

    
