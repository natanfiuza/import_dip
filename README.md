
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


```txt

/agente\_ia\_dip
├── .env          \# (Arquivo local para suas chaves e configurações)
├── .gitignore    \# (Define quais arquivos o Git deve ignorar)
├── Pipfile       \# (Gerado pelo pipenv, define as dependências)
├── Pipfile.lock  \# (Gerado pelo pipenv, garante builds determinísticos)
├── config.py     \# Módulo para carregar as configurações do .env
├── db\_manager.py \# Módulo para gerenciar a conexão e operações do MongoDB
├── import\_dip.py \# O script CLI principal
└── utils.py      \# Funções auxiliares (ex: carregar JSON)

```

## Instalação e Configuração

Siga estes passos para configurar o ambiente de desenvolvimento localmente.

### 1. Iniciar com Git (Novo Repositório)

Se você está a começar este projeto do zero no seu computador, é uma boa prática inicializá-lo com o Git para controlo de versão.

```bash
# 1. Navegue até a pasta onde você criou os arquivos Python
cd /caminho/para/agente_ia_dip

# 2. Inicialize um novo repositório Git
#    (O -b main define o nome da branch principal como "main")
git init -b main

# 3. Crie um arquivo .gitignore
#    É CRUCIAL para não enviar arquivos sensíveis (como .env)
#    ou pastas de ambiente (como .venv) para o seu repositório.
````

Crie um arquivo chamado `.gitignore` na raiz do projeto e adicione o seguinte conteúdo:

```gitignore
# Arquivos de ambiente Python
.venv/
__pycache__/
*.pyc

# Arquivo de variáveis de ambiente
.env

# Arquivos de sistema
.DS_Store
```

```bash
# 4. Adicione todos os arquivos (exceto os ignorados) ao Git
git add .

# 5. Crie o seu primeiro "commit" (um ponto de salvamento)
git commit -m "Commit inicial - Estrutura do importador DIP para MongoDB"
```

### 2\. Configurar Dependências com Pipenv

Este projeto usa `pipenv` para gerenciar as dependências e o ambiente virtual de forma isolada.

```bash
# 1. Na raiz do projeto, instale as dependências
#    Isso irá criar os arquivos Pipfile e Pipfile.lock
pipenv install pymongo python-dotenv

# 2. Ative o ambiente virtual
#    Todos os comandos Python devem ser executados após este passo.
pipenv shell
```

  * **`pymongo`**: O driver oficial do MongoDB para Python.
  * **`python-dotenv`**: Biblioteca usada para ler o arquivo `.env`.

### 3\. Configuração do Ambiente (`.env`)

Antes de executar o script, você deve criar um arquivo `.env` na raiz do projeto.

1.  Faça uma copia do arquivo:

    ```bash
    example.env -> .env
    ```

2.  Altere as seguintes variáveis, substituindo pelos seus dados reais:

    ```ini
    # Configurações do MongoDB
    # Exemplo para conexão local:
    MONGO_URI="mongodb://localhost:27017/"

    # Exemplo para conexão na nuvem (Atlas):
    # MONGO_URI="mongodb+srv://SEU_USUARIO:SUA_SENHA@SEU_CLUSTER.mongodb.net/?retryWrites=true&w=majority"

    MONGO_DB_NAME=""
    MONGO_COLLECTION_NAME=""
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

