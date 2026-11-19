import random
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI()

LOCATIONS = {"1": "Living Room", "2": "Bedroom", "3": "Kitchen"}
SENSOR_IDS = {"Living Room": "1", "Bedroom": "2", "Kitchen": "3"}


def temperature(location, sensor_id):
    if not location:
        location = LOCATIONS.get(sensor_id, "Unknown")
    if not sensor_id:
        sensor_id = SENSOR_IDS.get(location, "0")

    return {
        "value": round(random.uniform(18, 26), 1),
        "unit": "°C",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "location": location,
        "status": "active",
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "description": f"Temperature sensor in {location}",
    }


@app.get("/temperature")
def by_location(location: str = "", sensorId: str = ""):
    return temperature(location, sensorId)


@app.get("/temperature/{sensor_id}")
def by_sensor_id(sensor_id: str):
    return temperature("", sensor_id)
