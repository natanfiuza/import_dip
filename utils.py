# utils.py
import json

def load_json_file(filepath):
    """
    Carrega um arquivo JSON de um caminho especificado.
    
    Args:
        filepath (str): O caminho para o arquivo JSON.
        
    Returns:
        list: Os dados carregados do JSON (espera-se uma lista de documentos).
    
    Raises:
        FileNotFoundError: Se o arquivo não for encontrado.
        json.JSONDecodeError: Se o arquivo não for um JSON válido.
        Exception: Para outros erros inesperados.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Validação básica da estrutura
            if not isinstance(data, list):
                print(f"Erro: O JSON em '{filepath}' não contém uma lista de documentos na raiz.")
                return None
            if not all(isinstance(item, dict) for item in data):
                print(f"Erro: O JSON em '{filepath}' não contém uma lista de dicionários.")
                return None
                
            return data
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filepath}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{filepath}' não é um JSON válido.")
        return None
    except Exception as e:
        print(f"Um erro inesperado ocorreu ao ler o arquivo: {e}")
        return None