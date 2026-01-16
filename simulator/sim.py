import random
import json

import paho.mqtt.client as mqtt

import time

class Device:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type
        self.status = "online"
        self.battery_level = 100
        self.value = None

    # Generar una lectura simulada basada en el tipo de dispositivo
    def generate_reading(self):
        if self.battery_level > 0:
            self.battery_level -= 1
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
    def to_json(self):
        return json.dumps({
            "device_id": self.device_id,
            "device_type": self.device_type,
            "value": self.value,
            "status": self.status,
            "battery_level": self.battery_level
        })
        

client = mqtt.Client()
client.connect("localhost", 1883, 60)

dev = Device("001", "temperature_sensor")
print(f"Device ID: {dev.device_id}, Type: {dev.device_type}, Battery: {dev.battery_level}%")
topic = f"devices/{dev.device_id}/telemetry"

for i in range(5):
    dev.generate_reading()
    # Publicar el estado del dispositivo en el tópico MQTT
    client.publish(topic, payload=str(dev.to_json()), qos=0, retain=False)
    time.sleep(2)


