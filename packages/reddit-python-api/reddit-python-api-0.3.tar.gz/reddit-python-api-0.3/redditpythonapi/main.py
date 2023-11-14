from asyncio import run

from redditpythonapi import Reddit, SortType

APP_ID = "it1WGdzPV4kKb7v4Dxx6tg"
APP_SECRET = "DrUuAcKYjJhQV8xoRBNfCaTt354gZQ"
USER_AGENT = "Reddit API API (by Electronic-Mango on GitHub)"


async def main() -> None:
    reddit = Reddit(APP_ID, APP_SECRET, USER_AGENT)
    submissions1 = await reddit.subreddit_submissions("wow", 10, SortType.HOT)
    submissions2 = await reddit.subreddit_submissions("wow", 10, SortType.RISING)
    print()


if __name__ == "__main__":
    run(main())
