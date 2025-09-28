# Fast Car API

Uma API REST moderna para gerenciamento de carros, construída com FastAPI, SQLAlchemy e Poetry.

## Características

- **FastAPI**: Framework web moderno e performático
- **SQLAlchemy**: ORM poderoso para interação com banco de dados
- **Alembic**: Gerenciamento de migrações de banco de dados
- **Poetry**: Gerenciamento de dependências e ambiente virtual
- **Ruff**: Linting e formatação de código
- **Taskipy**: Automação de tarefas de desenvolvimento

## Estrutura do Projeto

```
fast_car_api/
├── src/
│   └── fast_car_api/
│       ├── __init__.py
│       ├── main.py              # Aplicação principal
│       ├── models.py            # Modelos SQLAlchemy
│       ├── schemas.py           # Schemas Pydantic
│       ├── routers.py           # Endpoints da API
│       └── database.py          # Configuração do banco
├── alembic/                     # Migrações do banco
├── tests/                       # Testes automatizados
├── pyproject.toml              # Configuração Poetry
├── alembic.ini                 # Configuração Alembic
└── README.md                   # Documentação
```

## Pré-requisitos

- Python 3.12+
- Poetry 1.4+

## Instalação

### 1. Clone o repositório

```bash
git clone <repository-url>
cd fast_car_api
```

### 2. Instale as dependências

```bash
poetry install
```

### 3. Configure o banco de dados

```bash
# Aplique as migrações
poetry run task migrate
```

### 4. Execute a aplicação

```bash
# Modo desenvolvimento
poetry run task dev

# Modo produção
poetry run task start
```

A API estará disponível em `http://127.0.0.1:8000`

## Documentação da API

Acesse a documentação interativa:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Endpoints

### Base URL: `/api/v1/cars`

| Método | Endpoint    | Descrição                | Status Code |
| ------ | ----------- | ------------------------ | ----------- |
| POST   | `/`         | Criar novo carro         | 201         |
| GET    | `/`         | Listar todos os carros   | 200         |
| GET    | `/{car_id}` | Obter carro por ID       | 200         |
| PUT    | `/{car_id}` | Atualizar carro completo | 201         |
| PATCH  | `/{car_id}` | Atualizar carro parcial  | 200         |
| DELETE | `/{car_id}` | Deletar carro            | 204         |

### Exemplos de Uso

#### Criar um carro

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/cars/" \
     -H "Content-Type: application/json" \
     -d '{
       "brand": "Ferrari",
       "color": "vermelho",
       "model": "F8 Tributo",
       "model_year": 2023,
       "factory_year": 2023,
       "description": "Supercarro italiano"
     }'
```

#### Listar carros

```bash
curl "http://127.0.0.1:8000/api/v1/cars/?offset=0&limit=10"
```

#### Obter carro específico

```bash
curl "http://127.0.0.1:8000/api/v1/cars/1"
```

#### Atualizar carro (completo)

```bash
curl -X PUT "http://127.0.0.1:8000/api/v1/cars/1" \
     -H "Content-Type: application/json" \
     -d '{
       "brand": "Lamborghini",
       "color": "amarelo",
       "model": "Huracán",
       "model_year": 2024,
       "factory_year": 2024,
       "description": "Supercarro atualizado"
     }'
```

#### Atualizar carro (parcial)

```bash
curl -X PATCH "http://127.0.0.1:8000/api/v1/cars/1" \
     -H "Content-Type: application/json" \
     -d '{
       "color": "azul",
       "description": "Cor atualizada"
     }'
```

#### Deletar carro

```bash
curl -X DELETE "http://127.0.0.1:8000/api/v1/cars/1"
```

## Schemas de Dados

### CarSchema (Entrada)

```json
{
  "brand": "string",
  "color": "string",
  "model": "string",
  "model_year": "integer",
  "factory_year": "integer",
  "description": "string (opcional)"
}
```

### CarSchemaPublic (Saída)

```json
{
  "id": "integer",
  "brand": "string",
  "color": "string",
  "model": "string",
  "model_year": "integer",
  "factory_year": "integer",
  "description": "string (opcional)"
}
```

### CarsList (Lista de carros)

```json
{
  "cars": [
    {
      "id": 1,
      "brand": "Ferrari",
      "color": "vermelho",
      "model": "F8 Tributo",
      "model_year": 2023,
      "factory_year": 2023,
      "description": "Supercarro italiano"
    }
  ]
}
```

## Comandos de Desenvolvimento

O projeto usa Taskipy para automação de tarefas:

```bash
# Verificar código
poetry run task lint

# Formatar código
poetry run task format

# Verificar formatação + linting
poetry run task check

# Executar aplicação em desenvolvimento
poetry run task dev

# Executar aplicação em produção
poetry run task start

# Aplicar migrações
poetry run task migrate

# Criar nova migração
poetry run task makemigration -m "descrição da mudança"

# Ver histórico de migrações
poetry run task migration-history

# Executar testes
poetry run task test

# Testes com cobertura
poetry run task test-cov

# Limpeza de arquivos temporários
poetry run task clean

# Pipeline completo (CI)
poetry run task ci
```

## Banco de Dados

O projeto usa SQLite por padrão para desenvolvimento. Para produção, você pode configurar PostgreSQL ou outro banco suportado pelo SQLAlchemy.

### Migrações

```bash
# Criar nova migração
poetry run alembic revision --autogenerate -m "descrição da mudança"

# Aplicar migrações
poetry run alembic upgrade head

# Reverter migração
poetry run alembic downgrade -1

# Ver histórico
poetry run alembic history
```

## Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=sqlite:///fast_car_api.db
DEBUG=True
```

## Desenvolvimento

### Adicionando novos endpoints

1. Defina o schema no `schemas.py`
2. Crie o endpoint no `routers.py`
3. Teste usando a documentação interativa
4. Execute os testes

### Estrutura de um endpoint

```python
@router.post(
    path="/",
    response_model=CarSchemaPublic,
    status_code=status.HTTP_201_CREATED,
    summary="Título do endpoint",
    description="Descrição detalhada do endpoint.",
)
def nome_funcao(parametros, session: Session = Depends(get_session)):
    """
    Docstring da função.
    """
    # Lógica do endpoint
    return resultado
```

## Tratamento de Erros

A API retorna erros padronizados:

### 404 - Não Encontrado

```json
{
  "detail": "Carro com ID 1 não encontrado"
}
```

### 422 - Erro de Validação

```json
{
  "detail": [
    {
      "type": "string_type",
      "loc": ["body", "brand"],
      "msg": "Input should be a valid string"
    }
  ]
}
```

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Add nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

### Padrões de Código

- Use Ruff para linting e formatação
- Escreva docstrings para funções públicas
- Mantenha linhas com máximo 79 caracteres
- Use imports relativos dentro do módulo

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Autor

**HiagoSilva** - [hiagosilvaanjos7@gmail.com](mailto:hiagosilvaanjos7@gmail.com)

## Changelog

### v0.1.0

- Implementação inicial da API
- CRUD completo para carros
- Documentação automática
- Sistema de migrações
- Configuração de desenvolvimento
