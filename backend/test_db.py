from db import init_db, insert_telemetry
import time

def run_test():
    init_db()

    insert_telemetry({
        "device_id": "dev001",
        "device_type": "temperature_sensor",
        "status": "online",
        "battery_level": 95,
        "value": 23.4,
        "ts": int(time.time())
    })

    insert_telemetry({
        "device_id": "dev002",
        "device_type": "humidity_sensor",
        "status": "low_battery",
        "battery_level": 18,
        "value": 72.1,
        "ts": int(time.time())
    })

    print("INSERT OK")

if __name__ == "__main__":
    run_test()
