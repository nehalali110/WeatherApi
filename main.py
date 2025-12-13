
from json import JSONDecodeError
from fastapi import Depends, FastAPI, Request
from models.endpoint_models import weatherReqParams
from visualCrossingApi.api_request import fetch_weather
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import redis
from RedisCache.cache import set_cache, get_cache

r = redis.Redis(host='localhost', port=6379, db=0)

app = FastAPI()

@app.get('/{location}')
def get_weather_by_location(request: Request, params: weatherReqParams = Depends(weatherReqParams)):
    return fetch_weather(request.url)


@app.get('/{location}/{datetime1}')
def get_weather_by_location_datetime1(request: Request, params: weatherReqParams = Depends(weatherReqParams)):
    return fetch_weather(request.url)
    


@app.get('/{location}/{datetime1}/{datetime2}')
def get_weather_by_location_datetime1_datetime2(request: Request, params: weatherReqParams = Depends(weatherReqParams)):
    return fetch_weather(request.url)



@app.exception_handler(RequestValidationError)
def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
            content={"status": "error", "msg": f"Invalid {exc.errors()[0]['loc'][1]} '{exc.errors()[0]['input']}'"},
            status_code=400
        )


@app.exception_handler(JSONDecodeError)
def json_validation_exception_handler(request: Request, exc: JSONDecodeError):
    address = request.url.path.replace("/", "")
    return JSONResponse(
            content={"status": "error", "msg": f"Invalid location '{address}'"}
        )

def main():
    print("Hello from weatherapi!")


if __name__ == "__main__":
    main()
