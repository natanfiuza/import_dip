# db_manager.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from config import config

def get_mongo_collection():
    """
    Cria uma conexão com o MongoDB e retorna a coleção desejada.
    
    Returns:
        pymongo.collection.Collection: O objeto da coleção do MongoDB.
    """
    try:
        # Conecta ao servidor MongoDB
        client = MongoClient(config.MONGO_URI)
        
        # Tenta acessar o banco de dados para verificar a conexão
        client.admin.command('ping') 
        
        # Acessa o banco de dados
        db = client[config.MONGO_DB_NAME]
        
        # Acessa a coleção
        collection = db[config.MONGO_COLLECTION_NAME]
        
        print(f"Conectado com sucesso ao MongoDB (DB: {config.MONGO_DB_NAME}, Collection: {config.MONGO_COLLECTION_NAME})")
        return collection
        
    except ConnectionFailure:
        print(f"Erro: Falha ao conectar ao MongoDB em {config.MONGO_URI}")
        return None
    except Exception as e:
        print(f"Um erro inesperado ocorreu na conexão com o MongoDB: {e}")
        return None

def import_data_to_mongo(collection, data):
    """
    Insere os dados (uma lista de documentos) na coleção do MongoDB.
    
    Args:
        collection (pymongo.collection.Collection): A coleção onde os dados serão inseridos.
        data (list): A lista de documentos (chunks) para inserir.
    """
    if not data:
        print("Nenhum dado para importar.")
        return

    try:
        # Limpa a coleção antes de inserir novos dados (Opcional, mas recomendado para DIP)
        print(f"Limpando a coleção '{config.MONGO_COLLECTION_NAME}' antes de importar...")
        collection.delete_many({})
        
        # Insere os novos dados
        print(f"Inserindo {len(data)} documentos...")
        result = collection.insert_many(data)
        
        print("\n--- Importação Concluída ---")
        print(f"Documentos inseridos com sucesso: {len(result.inserted_ids)}")
        
    except OperationFailure as e:
        print(f"Erro durante a operação no MongoDB: {e}")
    except Exception as e:
        print(f"Um erro inesperado ocorreu durante a inserção de dados: {e}")