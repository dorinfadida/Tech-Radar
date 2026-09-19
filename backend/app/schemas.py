from datetime import date

from pydantic import BaseModel


class Story(BaseModel):
    title: str
    summary: str


class DailyEdition(BaseModel):
    date: date
    top_story: Story