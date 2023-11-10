"""Support for sensors."""
import struct

from . import exceptions as e
from .device import Device


class motion(Device):
    """Controls a LinknLink motion."""

    TYPE = "MOTION"


class eths(Device):
    """Controls a LinknLink eths."""

    TYPE = "ETHS"

    def check_sensors(self) -> dict:
        """Return the state of the sensors."""
        resp = self._send(0x24)
        temp = struct.unpack("<bb", resp[:0x2])
        return {
            "temperature": temp[0x0] + temp[0x1] / 100.0,
            "humidity": resp[0x2] + resp[0x3] / 100.0,
        }

    def check_temperature(self) -> float:
        """Return the temperature."""
        return self.check_sensors()["temperature"]

    def check_humidity(self) -> float:
        """Return the humidity."""
        return self.check_sensors()["humidity"]