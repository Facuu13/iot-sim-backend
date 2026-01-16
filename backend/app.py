from fastapi import FastAPI
from mqtt_client import start_mqtt
from db import list_devices, get_latest


app = FastAPI()

mqtt_client = None


@app.on_event("startup")
def startup():
    global mqtt_client
    mqtt_client = start_mqtt()

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/devices")
def get_devices():
    devices = list_devices()
    return {"devices": devices}

@app.get("/devices/{device_id}")
def get_device_latest(device_id: str):
    telemetry = get_latest(device_id)
    if telemetry:
        return {"device": telemetry}
    else:
        return {"error": "Device not found"}