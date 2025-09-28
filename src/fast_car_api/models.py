from sqlalchemy import Column, Integer, String, Text

from src.fast_car_api.database import Base


class Car(Base):
    """
    Modelo de dados para representar um carro.
    """

    __tablename__ = "cars"  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=False)  # Marca do carro
    color = Column(String(30), nullable=False)  # Cor do carro
    model = Column(String(50), nullable=False)  # Modelo do carro
    model_year = Column(Integer, nullable=False)  # Ano do carro
    factory_year = Column(Integer, nullable=False)  # Ano de fabricação
    description = Column(Text, nullable=True)  # Descrição opcional
