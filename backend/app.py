from fastapi import FastAPI
from mqtt_client import start_mqtt

app = FastAPI()

mqtt_client = None


@app.on_event("startup")
def startup():
    global mqtt_client
    mqtt_client = start_mqtt()

@app.get("/health")
def health():
    return {"ok": True}
