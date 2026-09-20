from fastapi import FastAPI
from app.schemas import DailyEdition, Article
from app.database import get_connection
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

@app.get("/api/articles", response_model=list[Article])
def get_articles():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, title, content, url, published_at, summary, category
                FROM articles
                ORDER BY published_at DESC;
            """)

            rows = cursor.fetchall()

    return [
        Article(
            id=row[0],
            title=row[1],
            content=row[2],
            url=row[3],
            published_at=row[4],
            summary=row[5],
            category=row[6],
        )
        for row in rows
    ]