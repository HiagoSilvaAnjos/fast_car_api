from fastapi import FastAPI
from src.fast_car_api.routers import router as car_router
app = FastAPI(
    title="Fast Car API",
    description="Uma API rápida para gerenciar carros",
    version="1.0.0",
)

app.include_router(car_router)


@app.get("/")
def read_root():
    """
    Endpoint raiz que retorna uma mensagem de boas-vindas.
    """
    return {"message": "ok", "status": "200"}
