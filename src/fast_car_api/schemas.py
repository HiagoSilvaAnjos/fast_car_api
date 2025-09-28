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
    description: Optional[str] = None 

    class Config:
        from_attributes = True  

class CarPartialUpdateSchema(BaseModel):
    """
    Schema para atualização parcial de um carro.
    """
    brand: Optional[str] = None
    color: Optional[str] = None
    model: Optional[str] = None
    model_year: Optional[int] = None
    factory_year: Optional[int] = None
    description: Optional[str] = None

class CarsList(BaseModel):
    """
    Schema para retornar lista de carros.
    """
    cars: list[CarSchemaPublic]