#!/usr/bin/env python
# import_dip.py
import argparse
from config import config
from utils import load_json_file
from db_manager import get_mongo_collection, import_data_to_mongo

def main():
    """
    Função principal para executar o processo de importação via CLI.
    """
    # 1. Configuração do Parser de Argumentos
    parser = argparse.ArgumentParser(
        description="Agente IA - Importador do Pipeline de Ingestão de Dados (DIP)",
        epilog="Exemplo de uso: python import_dip.py --file /caminho/para/vetores.json"
    )
    
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Caminho para o arquivo JSON contendo os chunks, textos e vetores."
    )
    
    args = parser.parse_args()
    
    print("Iniciando o processo de importação...")

    # 2. Validar Configurações do .env
    if not config.validate():
        return # Encerra se as configurações estiverem faltando

    # 3. Carregar o arquivo JSON
    print(f"Carregando dados de '{args.file}'...")
    data_to_import = load_json_file(args.file)
    
    if data_to_import is None:
        print("Falha ao carregar dados. Encerrando.")
        return

    # 4. Obter a conexão com o MongoDB
    print("Conectando ao MongoDB...")
    collection = get_mongo_collection()
    
    if collection is None:
        print("Falha ao conectar ao banco de dados. Encerrando.")
        return

    # 5. Inserir os dados
    import_data_to_mongo(collection, data_to_import)

if __name__ == "__main__":
    main()