from fastapi import FastAPI

# Para ejecutar servidor --> uvicorn JurasicPark:app --reload

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "myresult"}

@app.get("/dinosaurio/")
async def get_dinosaurio():
    pass