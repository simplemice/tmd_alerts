from homeassistant.components.binary_sensor import BinarySensorEntity
from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([StormWarningBinary(coordinator)])


class StormWarningBinary(BinarySensorEntity):

    def __init__(self, coordinator):
        self.coordinator = coordinator
        self._attr_name = "Storm Warning Active"

    @property
    def is_on(self):
        for alert in self.coordinator.data:
            if "storm" in alert["title"].lower():
                return True
        return False
