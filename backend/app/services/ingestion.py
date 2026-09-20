from app.collectors.hacker_news import get_normalized_stories
from app.repositories.articles import save_article


def ingest_top_stories(limit: int = 10):
    articles = get_normalized_stories(limit)

    saved_count = 0
    skipped_count = 0

    for article in articles:
        article_id = save_article(article)

        if article_id is None:
            skipped_count += 1
        else:
            saved_count += 1

    return {
        "fetched": len(articles),
        "saved": saved_count,
        "skipped": skipped_count,
    }