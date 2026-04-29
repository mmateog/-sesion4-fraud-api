"""
Pydantic schemas: definen la forma EXACTA de los datos
que la API espera recibir y devolver.

ESTE ARCHIVO TIENE TODOs PARA QUE LOS COMPLETES EN CLASE.
"""

from pydantic import BaseModel, Field
from typing import Literal


# Categorias permitidas (las mismas que vio el modelo durante entrenamiento)
MerchantCategory = Literal[
    "grocery", "restaurant", "gas", "online", "electronics", "travel", "atm"
]


class TransactionInput(BaseModel):
    """Datos de una transaccion para predecir si es fraude."""

    # TODO 3: completa los campos. Cada uno debe tener tipo y descripcion.
    # Pistas:
    #   - amount: float, debe ser >= 0
    #   - hour: int, entre 0 y 23
    #   - merchant_category: MerchantCategory (es un Literal)
    #   - is_online: int, 0 o 1
    #   - is_foreign: int, 0 o 1
    #   - distance_from_home_km: float, >= 0
    #   - days_since_last_tx: float, >= 0
    #
    # Ejemplo de la sintaxis con Field:
    #   amount: float = Field(..., ge=0, description="Importe en euros")
    #
    # El "..." significa "obligatorio". ge = greater or equal. le = less or equal.

    pass  # ELIMINA esta linea cuando hayas anadido los campos


class PredictionOutput(BaseModel):
    """Resultado de una prediccion de fraude."""

    is_fraud: bool = Field(..., description="True si el modelo cree que es fraude")
    fraud_probability: float = Field(..., ge=0, le=1)
    model_version: str = Field(..., description="Version del modelo")

    model_config = {"protected_namespaces": ()}


class HealthResponse(BaseModel):
    """Estado del servicio."""

    status: Literal["ok", "degraded", "down"]
    model_loaded: bool
    model_version: str | None = None

    model_config = {"protected_namespaces": ()}
