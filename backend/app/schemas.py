from datetime import date
from datetime import datetime


from pydantic import BaseModel


class Story(BaseModel):
    title: str
    summary: str


class DailyEdition(BaseModel):
    date: date
    top_story: Story

class ArticleCreate(BaseModel):

    title: str
    content: str | None
    url: str
    published_at: datetime | None
    summary: str | None
    category: str | None

class Article(ArticleCreate):
    id: int