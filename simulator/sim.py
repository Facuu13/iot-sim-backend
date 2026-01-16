#incluir random

import random
import json

class Device:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type
        self.status = "offline"
        self.battery_level = 100

    # Generar una lectura simulada basada en el tipo de dispositivo
    def generate_reading(self):
        if self.battery_level > 0:
            self.battery_level -= 1
        if self.device_type == "temperature_sensor":
            return round(random.uniform(12.0, 50.0), 2)  # Temperatura en grados Celsius
        elif self.device_type == "humidity_sensor":
            return round(random.uniform(10.0, 90.0), 2)  # Humedad en porcentaje
        elif self.device_type == "pressure_sensor":
            return round(random.uniform(950.0, 1050.0), 2)  # Presión en hPa
        else:
            return None
    
    # Convertir el estado del dispositivo a JSON
    def to_json(self):
        return json.dumps({
            "device_id": self.device_id,
            "device_type": self.device_type,
            "status": self.status,
            "battery_level": self.battery_level
        })
        

dev = Device("001", "temperature_sensor")
print(f"Device ID: {dev.device_id}, Type: {dev.device_type}, Battery: {dev.battery_level}%")

reading = dev.generate_reading()
print(f"Generated Reading: {reading}, Battery Level: {dev.battery_level}%")
        
    