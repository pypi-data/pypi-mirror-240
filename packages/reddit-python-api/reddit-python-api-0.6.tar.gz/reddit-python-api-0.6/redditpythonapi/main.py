from asyncio import run

from redditpythonapi import ArticlesSortType, CommentsSortType, Reddit

APP_ID = "it1WGdzPV4kKb7v4Dxx6tg"
APP_SECRET = "DrUuAcKYjJhQV8xoRBNfCaTt354gZQ"
USER_AGENT = "Reddit API API (by Electronic-Mango on GitHub)"


async def main() -> None:
    reddit = Reddit(APP_ID, APP_SECRET, USER_AGENT)
    # articles1 = await reddit.subreddit_articles("wow", 10, ArticlesSortType.HOT)
    # articles2 = await reddit.subreddit_articles("wow", 10, ArticlesSortType.RISING)
    articles3 = await reddit.subreddit_article_comments(
        "wow", "17tpwfa", 10, CommentsSortType.CONFIDENCE
    )
    print()


if __name__ == "__main__":
    run(main())
