# Simulador de dispositivos IoT + mini backend

## Objetivo del proyecto
Simular N dispositivos que publican telemetría (temp, humedad, batería, estado) y un backend que:

* Recibe esos mensajes (por MQTT),

* Los guarda en SQLite,

* Expone una API REST para ver “últimas lecturas”, historial, y estados.


## Stack simple 

* MQTT broker: Mosquitto (en Docker)

* Simulator: Python (paho-mqtt)

* Backend API: FastAPI (o Flask si querés más simple)

* DB: SQLite (con SQLAlchemy o sqlite3 directo)

* (opcional) Dashboard: HTML/JS o algo mínimo

