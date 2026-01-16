import random
import json

import paho.mqtt.client as mqtt

import time

from enum import Enum

class DeviceStatus(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    LOW_BATTERY = "low_battery"
    ERROR = "error"


class Device:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type
        self.status = DeviceStatus.ONLINE.value
        self.battery_level = 100
        self.value = None

    #hacer un metodo para la bateria
    def update_battery(self):
        self.battery_level -= random.uniform(0.5, 2.0)
        if self.battery_level <= 0:
            self.status = DeviceStatus.OFFLINE.value
            self.battery_level = 0
        elif self.battery_level < 20:
            self.status = DeviceStatus.LOW_BATTERY.value
        else:
            self.status = DeviceStatus.ONLINE.value

    # Generar una lectura simulada basada en el tipo de dispositivo
    def generate_reading(self):
        self.update_battery()
        if self.device_type == "temperature_sensor":
            self.value = round(random.uniform(12.0, 50.0), 2)  # Temperatura en grados Celsius
            return self.value
        elif self.device_type == "humidity_sensor":
            self.value = round(random.uniform(10.0, 90.0), 2)  # Humedad en porcentaje
            return self.value
        elif self.device_type == "pressure_sensor":
            self.value = round(random.uniform(950.0, 1050.0), 2)  # Presión en hPa
            return self.value
        else:
            return None
    
    # Convertir el estado del dispositivo a JSON
    def to_dict(self):
        return {
            "device_id": self.device_id,
            "device_type": self.device_type,
            "status": self.status,
            "battery_level": self.battery_level,
            "value": self.value,
            "ts": int(time.time())
        }

        

client = mqtt.Client()
client.connect("localhost", 1883, 60)

devices = []
device_types = ["temperature_sensor", "humidity_sensor", "pressure_sensor"]
for i in range(10):
    dev_type = random.choice(device_types)
    dev = Device(f"{i:03d}", dev_type)
    devices.append(dev)


for _ in range(5):
    for dev in devices:
        dev.generate_reading()
        topic = f"devices/{dev.device_id}/telemetry"
        client.publish(topic, payload=json.dumps(dev.to_dict()), qos=0, retain=False)
    time.sleep(2)

