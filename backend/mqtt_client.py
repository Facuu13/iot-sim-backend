import paho.mqtt.client as mqtt

def star_mqtt(broker_url, broker_port):
    client = mqtt.Client()
    client.connect(broker_url, broker_port)
    return client

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

client = star_mqtt("localhost", 1883)
client.on_message = on_message

