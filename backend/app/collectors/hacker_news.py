import httpx
from datetime import datetime, timezone

from app.schemas import ArticleCreate


TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{item_id}.json"

def get_top_story_ids():
    response = httpx.get(TOP_STORIES_URL)
    return response.json()

def get_story(item_id: int):
    response = httpx.get(ITEM_URL.format(item_id=item_id))
    return response.json()


def normalize_story(story: dict) -> ArticleCreate:
    return ArticleCreate(
        title=story["title"],
        content=None,
        url=story["url"],
        published_at=datetime.fromtimestamp(
            story["time"],
            tz=timezone.utc
        ),
        summary=None,
        category=None,
    )

def get_top_stories(limit: int = 10):
    story_ids = get_top_story_ids()[:limit]

    stories = []

    for story_id in story_ids:
        story = get_story(story_id)

        if story is not None:
            stories.append(story)

    return stories

def get_normalized_stories(limit: int = 10) -> list[ArticleCreate]:
    stories = get_top_stories(limit)

    articles = []

    for story in stories:
        if "url" not in story:
            continue

        article = normalize_story(story)
        articles.append(article)

    return articles