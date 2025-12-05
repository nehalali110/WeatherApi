
from fastapi import FastAPI
import models.endpoint_models

app = FastAPI()

@app.get('/{location}')
def get_weather_by_location(location: str):
    return {"msg": f"{location} weather"}


@app.get('/{location}/{datetime1}/{datetime2}')
def get_weather_by_location_datetime(location: str, datetime1: models.endpoint_models.datetime1Format, datetime2: models.endpoint_models.datetime2Format):
        pass


def main():
    print("Hello from weatherapi!")


if __name__ == "__main__":
    main()
