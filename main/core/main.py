import os
import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()

OW_API_KEY= os.getenv("OPEN_WEATHER_API_KEY")
GEOCODING_URL = "https://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


app = FastAPI()
@app.get("/")
async def root():
  return {"greeting":"Hello world"}

@app.get("/wheater/{city}")
async def wheater (city:str):
  if (city.lower()!="bogota" and city.lower()!="medellin"):
    raise HTTPException(
      status_code=404,
      detail="Ciudad no encontrada"
    )
  weather = "25" if city.lower()=="bogota" else "32"
  if len(city) < 3:
    raise HTTPException(
      status_code=400,
      detail="Nombre de ciudad inválido"
    )
  return {
    "city": city, "weather": weather, "temperartura": "30"
  }

@app.get("/open/weather/geo/{city}")
async def openWeatherGeo(city: str):
  if not OW_API_KEY: 
    raise HTTPException(status_code=500, detail="Falta OPENWEATHER_API_KEY en .env")
  
  async with httpx.AsyncClient() as client:
    geo_response = await client.get(
      GEOCODING_URL, params={"q": city, "limit": 1, "appid": OW_API_KEY}, timeout=10
    )
    if geo_response.status_code != 200:
            raise HTTPException(status_code=502, detail="Error consultando geocoding en OpenWeather")

    geo_data = geo_response.json()
    if not geo_data:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")

    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

  return await OpenWeather(city, lat, lon)
  # return {
  #   "city": city,
  #   "lon": geo_data[0]["lon"],
  #   "lat": geo_data[0]["lat"],
  #   # "geo_data": geo_data[0]
  # }

@app.get("open/wheater/{city}/{lat}/{lon}")
async def OpenWeather(city: str, lat:str, lon:str):
  async with httpx.AsyncClient() as client:
    weather_response = await client.get(
      WEATHER_URL,
      params={"lat": lat, "lon": lon, "appid": OW_API_KEY, "units": "metric", "lang": "es"},
      timeout=10
    )

    if weather_response.status_code != 200:
      raise HTTPException(status_code=502, detail="Error consultando clima en OpenWeather")

    weather_data = weather_response.json()

    return {
      "city": city,
      "temperature": weather_data["main"]["temp"],
      "humidity": weather_data["main"]["humidity"],
      "description": weather_data["weather"][0]["description"]
    }