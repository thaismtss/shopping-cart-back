
# Shopping Cart Back

Api construida com flask que implementa o fluxo de carrinho com as funcionalidade de: Criação de carrinho, Adicição de item, alteração de quantidade e deleção de item do carrinho

## Stack utilizada

Flask, SQLAlchemy, Postgres



## Rodando localmente

Siga estas etapas para executar o projeto em sua máquina local:

1. **Clone o Repositório:**

Abra o terminal e execute o seguinte comando para clonar o repositório do GitHub:

```bash
  git clone git@github.com:thaismtss/shopping-cart-back.git
```

2. **Crie a Rede Docker:**

Se ainda não tiver sido feito, crie a rede Docker executando o seguinte comando:

```bash
docker network create -d bridge app-network
```

2. **Execute os Comandos:**

Navegue até o diretório do projeto clonado e execute os seguintes comandos:

```bash
  cp ./.env.example ./.env && docker compose up -d
```

A api ficará disponivel em: http://localhost:5000


## Referência

 - [Flask](https://flask.palletsprojects.com/en/3.0.x/)
 - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
 - [Pytest](https://docs.pytest.org/en/8.0.x/)


## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  docker exec shopping-cart-server  python -m pytest
```

