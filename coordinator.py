from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN, DEFAULT_SCAN_INTERVAL, RSS_URL
from .api import fetch_alerts


class TMDCoordinator(DataUpdateCoordinator):

    def __init__(self, hass):
        super().__init__(
            hass,
            logger=hass.data[DOMAIN]["logger"],
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )

    async def _async_update_data(self):
        return await fetch_alerts(RSS_URL)
