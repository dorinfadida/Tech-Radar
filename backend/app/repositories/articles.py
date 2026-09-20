from app.database import get_connection
from app.schemas import ArticleCreate


def save_article(article: ArticleCreate) -> int | None:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO articles
                    (title, content, url, published_at, summary, category)
                VALUES
                    (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING
                RETURNING id;
                """,
                (
                    article.title,
                    article.content,
                    article.url,
                    article.published_at,
                    article.summary,
                    article.category,
                ),
            )

            row = cursor.fetchone()

    if row is None:
        return None

    return row[0]