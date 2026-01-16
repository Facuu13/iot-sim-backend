import paho.mqtt.client as mqtt
from db import init_db, insert_telemetry
import json

TOPIC = "devices/+/telemetry"

# Definir la función de callback para la conexión
def on_connect(client, userdata, flags, rc):
    print("Conectado con código de resultado: " + str(rc))
    client.subscribe(TOPIC)

# Definir la función de callback para la recepción de mensajes
def on_message(client, userdata, msg):
    payload_str = msg.payload.decode('utf-8')
    data = json.loads(payload_str)
    insert_telemetry(data)
    print(f"Datos insertados en la base de datos: {data}")

def main():
    # Inicializar la base de datos
    init_db()

    # Configurar el cliente MQTT
    client = mqtt.Client()

    # Asignar callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    # Conectar al broker MQTT
    client.connect("localhost", 1883, 60)

    # Iniciar el loop del cliente MQTT
    client.loop_forever()

if __name__ == "__main__":
    main()