from fastapi import APIRouter, status, Depends
from .schemas import CarSchema, CarSchemaPublic
from .models import Car
from .database import get_session
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/v1/cars", tags=["Cars"])


@router.post(
    path="/",
    response_model=CarSchemaPublic,
    status_code=status.HTTP_201_CREATED,
    summary="Criação de um novo carro",
    description="Endpoint para criar um novo carro na base de dados.",
)
#  essa função depende de uma sessão do banco de dados, cria uma nova sessão e depois fecha a sessão
def create_car(car: CarSchema, session: Session = Depends(get_session)):
    """
    Endpoint que cria um novo carro.
    """

    # 1 => Cria uma instância do modelo Car com os dados recebidos
    car = Car(**car.model_dump())
    print(f"Carro a ser criado: {car}")
    # 2 => Adiciona o carro na sessão do banco de dados
    session.add(car)
    # 3 => Salva as alterações no banco de dados
    session.commit()
    # 4 => Atualiza a instância do carro com os dados do banco de dados (como o ID gerado)
    session.refresh(car)
    # 5 => Retorna o carro criado
    return car
