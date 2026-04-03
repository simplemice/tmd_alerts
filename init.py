from homeassistant.core import HomeAssistant
import logging

from .const import DOMAIN
from .coordinator import TMDCoordinator

PLATFORMS = ["sensor", "binary_sensor"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]["logger"] = logging.getLogger(__name__)

    coordinator = TMDCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True
