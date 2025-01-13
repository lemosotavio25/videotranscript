import gspread
from google.oauth2.service_account import Credentials

def authenticate_google_sheets(credentials_file="credenciais.json", scopes=None):
    """
    Autentica no Google Sheets e retorna o cliente autenticado.
    
    :param credentials_file: Caminho para o arquivo de credenciais JSON.
    :param scopes: Lista de escopos necessários para a autenticação.
    :return: Cliente gspread autenticado.
    """
    try:
        if scopes is None:
            scopes = [
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive"
            ]
        
        print("Configurando as credenciais...")
        credentials = Credentials.from_service_account_file(credentials_file, scopes=scopes)
        print("Credenciais carregadas com sucesso!")

        print("Autorizando cliente do Google Sheets...")
        client = gspread.authorize(credentials)
        print("Cliente autorizado com sucesso!")
        
        return client

    except FileNotFoundError:
        print("Erro: O arquivo 'credenciais.json' não foi encontrado. Verifique o caminho.")
        raise
    except gspread.exceptions.APIError as api_error:
        print(f"Erro na API do Google: {api_error}")
        raise
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise