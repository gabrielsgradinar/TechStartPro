# Desafio

Para para atender os requisitos propóstos desafio foi feito a criação de uma API com Python utilizando o framework FastAPI para realizar o CRUD do produto e a inserção das categorias via arquivo csv.

## Instalação das dependencia para execução do projeto e testes
>  * Para a instalação das dependencia é necessário ter Python 3.x e o gerenciador de pacotes do Python instalado o **pip**
>  * Na pasta raiz do projeto executar **pip install -r requirements.txt**
>  * Entre na pasta **/app** e execute o comando **uvicorn main:app --reload** para executar a API que ficará disponivel no endereço [http://127.0.0.1:8000](http://127.0.0.1:8000)
>  *  As rotas disponiveis são:
>  *  POST - */product/* - cadastro do produto
>  *  GET - */products/* - busca todos os produtos
>  *  PUT - */product/{id}/* - faz a atualização parcial do produto pelo id
>  *  DELETE - */product/{id}/* - faz a exclusão do produto pelo id
>  *  GET - */category/file* - faz a inserção de categorias apartir de um csv fixo dentro do projeto
>  *  GET - */categories/* - busca todos as categorias
>  *  *No endereço [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) é possivel encontrar uma documentação utilizando o Swagger gerado pelo proprio FastAPI*
>  * Para realizar os testes execute o comando **python -m pytest -v tests/** dentro da pasta **app**

## Ambiente de desenvolvimento
>  * Computador: Notebook, Intel Core I5, 8GB RAM e 128GB SSD + 1TB HDD
>  * Sistema operacional: Pop!_OS 20.10
>  * Editor de Texto / IDE: Visual Studio Code + Extensões

As principais tecnologias utilizadas no projeto foram:
>  * Framework FastAPI - framework para a criação das rotas da API
>  * SQLAlchemy - ORM utilizado para criação dos modelos do banco de dados
>  * Pydantic - biblioteca utilizada para a validação de dados nas requisições da API
>  * Pytest - Framework para a realização dos testes




