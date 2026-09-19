from fastapi import FastAPI
from app.schemas import DailyEdition
app = FastAPI(title="TechRadar API")


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/editions/today", response_model=DailyEdition)
def get_today_edition():
    return {
        "date": "2026-09-19",
        "top_story": {
            "title": "TechRadar is alive!",
            "summary": "The first TechRadar Daily Edition."
        }
    }