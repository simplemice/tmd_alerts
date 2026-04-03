import feedparser

async def fetch_alerts(url):
    feed = feedparser.parse(url)

    alerts = []

    for entry in feed.entries:
        alerts.append({
            "title": entry.title,
            "summary": entry.summary,
            "published": entry.published,
        })

    return alerts
