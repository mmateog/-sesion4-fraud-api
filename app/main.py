"""
API REST para servir el modelo de deteccion de fraude.

Para arrancar localmente:
    uvicorn app.main:app --reload

Documentacion interactiva en: http://localhost:8000/docs

ESTE ARCHIVO TIENE TODOs PARA QUE LOS COMPLETES EN CLASE.
"""

import logging
import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

from app.ml_model import fraud_model
from app.schemas import TransactionInput, PredictionOutput, HealthResponse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("fraud-api")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Cargamos el modelo al arrancar la API."""
    logger.info("Arrancando API de deteccion de fraude...")
    fraud_model.load()
    logger.info("Modelo cargado y listo")
    yield
    logger.info("Apagando API...")


app = FastAPI(
    title="Fraud Detection API",
    description="API para detectar transacciones fraudulentas",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def root():
    """Saludo basico."""
    return {
        "service": "fraud-detection-api",
        "docs": "/docs",
        "health": "/health",
    }


# TODO 1: implementar el endpoint GET /health
# Pista: usa response_model=HealthResponse
# Si fraud_model.is_loaded() devuelve True, el status es "ok".
# Si no, el status es "down".


# TODO 2: implementar el endpoint POST /predict
# Pista: recibe un objeto TransactionInput, devuelve un PredictionOutput.
# Pasos dentro del endpoint:
#   1. Llamar a fraud_model.predict(transaction.model_dump())
#      Devuelve una tupla (is_fraud, fraud_probability)
#   2. Loguear la prediccion con logger.info(...)
#   3. Devolver un PredictionOutput con los datos
# Manejo de errores: envuelve la prediccion en un try/except y, si falla,
# lanza HTTPException(status_code=500, detail=...)
