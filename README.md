
# Agente IA - Importador do Pipeline de Ingestão de Dados (DIP)

Este é um script Python de linha de comando (CLI), a sua principal função é ler um arquivo JSON — contendo os *chunks* de texto e os *vetores de embedding* — e importá-los em massa para uma coleção específica no MongoDB.

## Funcionalidades

* **Interface de Linha de Comando (CLI):** Fácil de usar, aceita o caminho do arquivo JSON como argumento.
* **Configuração Segura:** Carrega informações sensíveis (string de conexão do MongoDB, nomes de banco e coleção) a partir de um arquivo `.env`.
* **Código Modular:** O projeto é dividido em módulos para facilitar a manutenção (`config.py`, `db_manager.py`, `utils.py`).
* **Gestão de Dados:** O script primeiro limpa a coleção de destino antes de inserir os novos dados, garantindo que apenas os dados da última importação estejam presentes.

## Pré-requisitos

Antes de começar, garanta que você tem as seguintes ferramentas instaladas:

* [Python (3.8+ recomendado)](https://www.python.org/downloads/)
* [pipenv](https://pipenv.pypa.io/en/latest/installation.html) (para gestão de pacotes e ambiente virtual)
* [Git](https://git-scm.com/downloads) (para controle de versão)
* Acesso a um servidor MongoDB (local ou na nuvem, como o MongoDB Atlas).

## Estrutura do Projeto

```

/import_dip
├── .env                # (Arquivo local para suas chaves e configurações - NÃO É ENVIADO AO GIT)
├── .gitignore          # (Define quais arquivos o Git deve ignorar)
├── example.env         # (Arquivo de exemplo para as variáveis de ambiente)
├── Pipfile             # (Gerado pelo pipenv, define as dependências)
├── Pipfile.lock        # (Gerado pelo pipenv, garante builds determinísticos)
├── requirements.txt    # (Lista de dependências para ambientes sem pipenv)
├── config.py           # Módulo para carregar as configurações do .env
├── db_manager.py       # Módulo para gerenciar a conexão e operações do MongoDB
├── import_dip.py       # O script CLI principal
└── utils.py            # Funções auxiliares (ex: carregar JSON)

````

## Instalação e Configuração

Siga estes passos para configurar o ambiente de desenvolvimento localmente.

### 1. Clonar o Repositório

Primeiro, clone o repositório do GitHub para o seu computador local usando o terminal.

```bash
# 1. Clone o repositório
git clone [https://github.com/natanfiuza/import_dip.git](https://github.com/natanfiuza/import_dip.git)

# 2. Entre na pasta do projeto
cd import_dip
````

### 2\. Configurar Dependências com Pipenv

Este projeto usa `pipenv` para gerenciar as dependências e o ambiente virtual de forma isolada. O `Pipfile` na raiz do projeto já contém todas as dependências necessárias.

```bash
# 1. Na raiz do projeto, instale as dependências listadas no Pipfile
#    Isso irá criar o ambiente virtual (.venv) e instalar os pacotes.
pipenv install

# 2. Ative o ambiente virtual
#    Todos os comandos Python devem ser executados após este passo.
pipenv shell
```

As principais dependências instaladas são:

  * **`pymongo`**: O driver oficial do MongoDB para Python.
  * **`python-dotenv`**: Biblioteca usada para ler o arquivo `.env`.

*(Nota: O arquivo `requirements.txt` também é fornecido caso você prefira usar `pip` e `venv` tradicionais, mas `pipenv` é o método recomendado para este projeto.)*

### 3\. Configuração do Ambiente (`.env`)

Antes de executar o script, você deve criar um arquivo `.env` para armazenar suas chaves de API e strings de conexão de forma segura.

1.  Copie o arquivo de exemplo `example.env` para criar o seu arquivo `.env` local:

    ```bash
    cp example.env .env
    ```

    *(O arquivo `.env` já está no `.gitignore`, por isso ele nunca será enviado para o repositório e manterá as suas chaves seguras.)*

2.  Abra o arquivo `.env` com seu editor de texto e altere as variáveis, substituindo pelos seus dados reais:

    ```ini
    # Configurações do MongoDB
    # Exemplo para conexão local:
    MONGO_URI="mongodb://localhost:27017/"

    # Exemplo para conexão na nuvem (Atlas):
    # MONGO_URI="mongodb+srv://SEU_USUARIO:SUA_SENHA@SEU_CLUSTER.mongodb.net/?retryWrites=true&w=majority"

    MONGO_DB_NAME="agente_ia_livro"
    MONGO_COLLECTION_NAME="regras_de_vida_vetores"
    ```

## Como Usar

Certifique-se de que o seu ambiente `pipenv` está ativo (`pipenv shell`).

### 1\. Ver a Ajuda

Para ver a mensagem de ajuda e todos os argumentos disponíveis, use `-h` ou `--help`:

```bash
python import_dip.py -h
```

Saída esperada:

```
usage: import_dip.py [-h] --file FILE

Agente IA - Importador do Pipeline de Ingestão de Dados (DIP)

options:
  -h, --help   show this help message and exit
  --file FILE  Caminho para o arquivo JSON contendo os chunks, textos e vetores.

Exemplo de uso: python import_dip.py --file /caminho/para/vetores.json
```

### 2\. Executar a Importação

Para executar o script, você deve fornecer o caminho para o seu arquivo JSON de vetores usando o argumento obrigatório `--file`.

```bash
# Substitua pelo caminho real do seu arquivo
python import_dip.py --file /caminho/completo/para/vetores.json
```

**Exemplo de sucesso na execução:**

```
$ python import_dip.py --file ./meus_vetores.json
Iniciando o processo de importação...
Carregando dados de './meus_vetores.json'...
Conectando ao MongoDB...
Conectado com sucesso ao MongoDB (DB: agente_ia_livro, Collection: regras_de_vida_vetores)
Limpando a coleção 'regras_de_vida_vetores' antes de importar...
Inserindo 1234 documentos...

--- Importação Concluída ---
Documentos inseridos com sucesso: 1234
```

