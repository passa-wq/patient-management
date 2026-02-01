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

## ERD-Diagramm
```mermaid
erDiagram
    PATIENT {
        int id
        string vorname
        string nachname
        date geburtsdatum
        string email
        string telefon
        string krankengeschichte
    }
