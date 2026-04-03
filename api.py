import feedparser
from homeassistant.core import HomeAssistant

async def fetch_alerts(hass: HomeAssistant, url: str):
    """Fetch and parse RSS feed in the executor to avoid blocking."""
    def parse():
        return feedparser.parse(url)

    feed = await hass.async_add_executor_job(parse)
    
    alerts = []
    for entry in feed.entries:
        alerts.append({
            "title": entry.get("title", "No Title"),
            "summary": entry.get("summary", ""),
            "published": entry.get("published", ""),
        })
    return alerts
