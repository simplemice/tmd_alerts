
async def async_setup(hass: HomeAssistant, config: dict):
    """Set up integration via YAML (unused but REQUIRED)."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up TMD Alerts from config entry."""

    coordinator = TMDCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload config entry."""
    return await hass.config_entries.async_unload_platforms(
        entry, PLATFORMS
    )
