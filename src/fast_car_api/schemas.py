from pydantic import BaseModel
from typing import Optional


# Contrato de dados para um carro
class CarSchema(BaseModel):
    """
    Esquema Pydantic para representar um carro.
    """

    brand: str
    color: str
    model: str
    model_year: int
    factory_year: int
    description: Optional[str] = None


class CarSchemaPublic(BaseModel):
    """
    Esquema Pydantic para representar um carro.
    """

    id: int
    brand: str
    color: str
    model: str
    model_year: int
    factory_year: int
    description: str
