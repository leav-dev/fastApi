from fastapi import FastAPI, HTTPException
app = FastAPI()
@app.get("/")
async def root():
  return {"greeting":"Hello world"}

@app.get("/test")
async def test():
    return {"greeting": "200 OK"}

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