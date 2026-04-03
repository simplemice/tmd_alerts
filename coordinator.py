from datetime import timedelta
import logging
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL, RSS_URL
from .api import fetch_alerts

_LOGGER = logging.getLogger(__name__)

class TMDCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, entry):
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.region = entry.data.get("region", "All")

    async def _async_update_data(self):
        try:
            alerts = await fetch_alerts(self.hass, RSS_URL)
            if self.region == "All":
                return alerts
            # Filter based on region selected in Config Flow
            return [a for a in alerts if self.region.lower() in a["title"].lower()]
        except Exception as err:
            raise UpdateFailed(f"Error communicating with TMD API: {err}")
