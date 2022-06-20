## Ritual-log
Ritual-log é um CLI-APP para realizar CRUD dos rituais do RPG de mesa [Ordem Paranormal](https://ordemparanormal.com.br/).

### Como planos futuros para essa aplicação temos:
- Disponibilizar as informações cadastradas no banco de dados através de uma API, para ser consumida por outras aplicações no futuro;
- Implementação de Testes;
- Otimização do codigo.

## Requisitos
- [Python3.8+](https://www.python.org/) ou superior;
- Esse repositório utiliza o gerenciador de pacotes [**Poetry**](https://python-poetry.org/);

### Após instalar o python (Orientações no site)

#### Se estiver rodando no Linux no seu ambiente local

`execute o comando abaixo para instalar o Poetry no Linux`

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

#### Em outros ambientes pode instalar com`

```bash
pip install --user poetry
```

## Preparando o ambiente

`após instalar os requisitos vamos usar o poetry pra instalar as demais dependencias`


O comando a seguir instala as dependências do projeto.

```bash
poetry install
```

O comando a seguir ativa o ambiente virtual do poetry

```bash
poetry shell
```

Ou execute `source start_poetry` que é um script que automatiza os comandos acima.

> **IMPORTANTE** o ambiente precisa estar ativado para o programa executar.  

Executando o programa

```bash
rituallog --help
# ou
python -m rituallog --help
```
> Se tudo correu bem o prograva deve printar um help com a documentação da CLI.
