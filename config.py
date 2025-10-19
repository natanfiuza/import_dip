# config.py
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

class Config:
    """
    Classe de configuração para carregar variáveis de ambiente.
    """
    MONGO_URI = os.getenv('MONGO_URI')
    MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
    MONGO_COLLECTION_NAME = os.getenv('MONGO_COLLECTION_NAME')

    @staticmethod
    def validate():
        """Verifica se todas as variáveis essenciais foram carregadas."""
        if not all([Config.MONGO_URI, Config.MONGO_DB_NAME, Config.MONGO_COLLECTION_NAME]):
            print("Erro: Nem todas as variáveis de ambiente do MongoDB estão definidas.")
            print("Verifique seu arquivo .env e se ele contém:")
            print("MONGO_URI, MONGO_DB_NAME, MONGO_COLLECTION_NAME")
            return False
        return True

# Instância única para ser importada por outros módulos
config = Config()