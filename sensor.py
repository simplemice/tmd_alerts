from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([TMDAlertSensor(coordinator)])


class TMDAlertSensor(SensorEntity):

    def __init__(self, coordinator):
        self.coordinator = coordinator
        self._attr_name = "TMD Weather Alerts"

    @property
    def state(self):
        return len(self.coordinator.data)

    @property
    def extra_state_attributes(self):
        return {"alerts": self.coordinator.data}

    async def async_update(self):
        await self.coordinator.async_request_refresh()
