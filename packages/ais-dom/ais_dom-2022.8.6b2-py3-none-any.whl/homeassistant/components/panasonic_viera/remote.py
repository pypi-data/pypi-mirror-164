"""Remote control support for Panasonic Viera TV."""
from __future__ import annotations

from homeassistant.components.remote import RemoteEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME, STATE_ON
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    ATTR_DEVICE_INFO,
    ATTR_MANUFACTURER,
    ATTR_MODEL_NUMBER,
    ATTR_REMOTE,
    ATTR_UDN,
    DEFAULT_MANUFACTURER,
    DEFAULT_MODEL_NUMBER,
    DOMAIN,
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Panasonic Viera TV Remote from a config entry."""

    config = config_entry.data

    remote = hass.data[DOMAIN][config_entry.entry_id][ATTR_REMOTE]
    name = config[CONF_NAME]
    device_info = config[ATTR_DEVICE_INFO]

    async_add_entities([PanasonicVieraRemoteEntity(remote, name, device_info)])


class PanasonicVieraRemoteEntity(RemoteEntity):
    """Representation of a Panasonic Viera TV Remote."""

    def __init__(self, remote, name, device_info):
        """Initialize the entity."""
        # Save a reference to the imported class
        self._remote = remote
        self._name = name
        self._device_info = device_info

    @property
    def unique_id(self):
        """Return the unique ID of the device."""
        if self._device_info is None:
            return None
        return self._device_info[ATTR_UDN]

    @property
    def device_info(self) -> DeviceInfo | None:
        """Return device specific attributes."""
        if self._device_info is None:
            return None
        return DeviceInfo(
            identifiers={(DOMAIN, self._device_info[ATTR_UDN])},
            manufacturer=self._device_info.get(ATTR_MANUFACTURER, DEFAULT_MANUFACTURER),
            model=self._device_info.get(ATTR_MODEL_NUMBER, DEFAULT_MODEL_NUMBER),
            name=self._name,
        )

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def available(self):
        """Return True if the device is available."""
        return self._remote.available

    @property
    def is_on(self):
        """Return true if device is on."""
        return self._remote.state == STATE_ON

    async def async_turn_on(self, **kwargs):
        """Turn the device on."""
        await self._remote.async_turn_on(context=self._context)

    async def async_turn_off(self, **kwargs):
        """Turn the device off."""
        await self._remote.async_turn_off()

    async def async_send_command(self, command, **kwargs):
        """Send a command to one device."""
        for cmd in command:
            await self._remote.async_send_key(cmd)
