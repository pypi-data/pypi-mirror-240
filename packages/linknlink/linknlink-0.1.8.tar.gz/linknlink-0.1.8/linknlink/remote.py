"""Support for universal remotes."""
import struct

from . import exceptions as e
from .device import Device

class ehub(Device):
    """Controls a LinknLink ehub."""

    TYPE = "EHUB"
        
    def _send(self, command: int, data: bytes = b"") -> bytes:
        """Send a packet to the device."""
        packet = struct.pack("<HI", len(data) + 4, command) + data
        resp = self.send_packet(0x6A, packet)
        e.check_error(resp[0x22:0x24])
        payload = self.decrypt(resp[0x38:])
        p_len = struct.unpack("<H", payload[:0x2])[0]
        return payload[0x6 : p_len + 2]
    
    def check_sensors(self) -> dict:
        """Return the state of the sensors."""
        resp = self._send(0x24)
        return {
            "envtemp": resp[0x0] + resp[0x1] / 100.0,
            "envhumid": resp[0x2] + resp[0x3] / 100.0,
            "pir_detected": resp[0x6],
        }

    def check_temperature(self) -> float:
        """Return the temperature."""
        return self.check_sensors()["temperature"]

    def check_humidity(self) -> float:
        """Return the humidity."""
        return self.check_sensors()["humidity"]
    
    def check_pir(self) -> int:
        """Return the pirDetected."""
        return self.check_sensors()["pirDetected"]