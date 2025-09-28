from fastapi import APIRouter, status, Depends, HTTPException
from src.fast_car_api.schemas import CarSchema, CarSchemaPublic, CarsList, CarPartialUpdateSchema
from src.fast_car_api.models import Car 
from src.fast_car_api.database import get_session
from sqlalchemy.orm import Session
from sqlalchemy import select

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
    ---
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

@router.get(
    path="/",
    response_model=CarsList,
    status_code=status.HTTP_200_OK,
    summary="Listagem de carros",
    description="Endpoint para listar todos os carros na base de dados.",
)
def get_cars(session: Session = Depends(get_session), offset: int = 0, limit: int = 100):
    """
    Endpoint que retorna uma lista de carros.
    ---
    """

    # 1 => Consulta todos os carros no banco de dados
    query = session.scalars(select(Car).offset(offset).limit(limit))
    cars = query.all()
    # 2 => Retorna a lista de carros
    return {"cars": cars}
   

@router.get(
    path="/{card_id}",
    response_model=CarSchemaPublic,
    status_code=status.HTTP_200_OK,
    summary="Obter detalhes de um carro",
    description="Endpoint para obter os detalhes de um carro específico pelo seu ID.",
)
def get_car(car_id: int, session: Session = Depends(get_session)):
    """
    Endpoint que retorna os detalhes de um carro específico.
    ---
    """
    # 1 => Consulta o carro pelo ID no banco de dados
    car = session.get(Car, car_id)
    # 2 => Se o carro não for encontrado, lança uma exceção HTTP 404
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Carro com ID {car_id} não encontrado",
        )
    # 3 => Retorna o carro encontrado
    return car

@router.put(
    path="/{car_id}",
    response_model=CarSchemaPublic,
    status_code=status.HTTP_201_CREATED,
    summary="Atualizar um carro",
    description="Endpoint para atualizar os dados de um carro específico pelo seu ID.",
)

def update_car(car_id: int, car: CarSchema, session: Session = Depends(get_session)):
    """
    Endpoint que atualiza os dados de um carro específico.
    """

    # 1 => Consultar o carro pelo ID no banco de dados
    existing_car = session.get(Car, car_id)
    # 2 => Se o carro não for encontrado, lança uma exceção HTTP 404
    if not existing_car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Carro com ID {car_id} não encontrado",
        )
    
    # 3 => Atualiza os campos do carro existente com os novos dados
    for field, value in car.model_dump().items():
        setattr(existing_car, field, value)
    session.commit()
    session.refresh(existing_car)
    # 4 => Retorna o carro atualizado
    return existing_car

@router.patch(
    path="/{car_id}",
    response_model=CarSchemaPublic,
    status_code=status.HTTP_200_OK,
    summary="Atualização parcial de um carro",
    description="Endpoint para atualizar parcialmente os dados de um carro específico pelo seu ID.",
)

def patch_car(car_id: int, car: CarPartialUpdateSchema, session: Session = Depends(get_session)):
    """
    Endpoint que atualiza parcialmente os dados de um carro específico.
    """

    # 1 => Consultar o carro pelo ID no banco de dados
    existing_car = session.get(Car, car_id)
    # 2 => Se o carro não for encontrado, lança uma exceção HTTP 404
    if not existing_car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Carro com ID {car_id} não encontrado",
        )
    
    # 3 => Atualiza apenas os campos fornecidos no corpo da requisição
    car_data = car.model_dump(exclude_unset=True)
    for field, value in car_data.items():
        setattr(existing_car, field, value)
    session.commit()
    session.refresh(existing_car)
    # 4 => Retorna o carro atualizado
    return existing_car

@router.delete(
    path = "/{car_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletar um carro",
    description="Endpoint para deletar um carro específico pelo seu ID.",
)

def delete_car(car_id: int, session: Session = Depends(get_session)):
    """
    Endpoint que deleta um carro específico.
    """

    # 1 => Consultar o carro pelo ID no banco de dados
    existing_car = session.get(Car, car_id)
    # 2 => Se o carro não for encontrado, lança uma exceção HTTP 404
    if not existing_car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Carro com ID {car_id} não encontrado",
        )
    
    # 3 => Deleta o carro do banco de dados
    session.delete(existing_car)
    session.commit()
    return None