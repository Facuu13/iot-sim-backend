# Simulador de dispositivos IoT + mini backend

## Objetivo del proyecto

Simular **N dispositivos** que publican telemetría (temp, humedad, batería, estado) y un **backend** que:

* recibe esos mensajes (por MQTT),
* los guarda en **SQLite**,
* expone una **API REST** para ver “últimas lecturas”, historial, y estados.

---

## Stack simple 

* **MQTT broker**: Mosquitto (en Docker)
* **Simulator**: Python (paho-mqtt)
* **Backend API**: FastAPI (o Flask si querés más simple)
* **DB**: SQLite (con SQLAlchemy o sqlite3 directo)
* (opcional) **Dashboard**: HTML/JS o algo mínimo

---

## Estructura de repo

```
iot-sim-backend/
  docker/
    docker-compose.yml
  simulator/
    sim.py
    devices.json
  backend/
    app.py
    db.py
    models.py
    mqtt_client.py
  README.md
```

---

## Data model mínimo 

### Tabla `telemetry`

* id (pk)
* device_id (string)
* ts (datetime)
* temp (float)
* hum (float)
* battery (float)
* rssi (int)
* status (string: "OK", "WARN", "ERROR")

### Tabla `device_state` (último estado)

* device_id (pk)
* last_seen (datetime)
* last_status (string)
* fw_version (string opcional)

---

## Mensajes MQTT (definimos “contrato”)

### Topic

`devices/{device_id}/telemetry`

### Payload JSON

```json
{
  "ts": "2026-01-15T21:05:00Z",
  "temp": 23.4,
  "hum": 56.0,
  "battery": 92.3,
  "rssi": -61,
  "status": "OK"
}
```

---

## API REST mínima

1. `GET /devices`
   Devuelve lista de dispositivos con last_seen + status

2. `GET /devices/{id}/latest`
   Última lectura

3. `GET /devices/{id}/telemetry?limit=100`
   Historial

4. `GET /health`
   para saber que vive

---

---

## Extras (para subir “nivel entrevista”)

Elegí 1 cuando ya esté todo andando:

* **Reglas**: si battery < 20 → status WARN
* **Offline detector**: si last_seen > X seg → device OFFLINE (calculado en API)
* **Autenticación**: API key simple
* **Tests**: 2–3 tests (API + parser de mensajes)
* **Dockerizar backend** también

---
