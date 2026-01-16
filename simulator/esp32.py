import network
import time
from umqtt.simple import MQTTClient
import ujson

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect("quepasapatejode", "losvilla08")

while not wlan.isconnected():
    time.sleep(0.2)

print("WiFi OK")
print(wlan.ifconfig())


client = MQTTClient(
    client_id="esp32_test",
    server="192.168.1.11",   # IP DE TU PC
    port=1883
)

client.connect()
print("MQTT connected")

client.publish("devices/esp32_test/telemetry", "hello from esp32")
print("published")


payload = {
    "device_id": "esp32_test",
    "device_type": "temperature_sensor",
    "value": 25.3,
    "status": "online",
    "battery_level": 100,
    "ts": int(time.time())
}

msg = ujson.dumps(payload)
client.publish("devices/esp32_test/telemetry", msg)
print(msg)