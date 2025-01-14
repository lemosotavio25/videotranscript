from goauth_service.gservice import authenticate_google_sheets
from table_manager.table import TableManager

def main():
    try:
        # Autenticar no Google Sheets
        print("Autenticando no Google Sheets...")
        client = authenticate_google_sheets()
        print("Autenticação concluída!")

        # Inicializar o gerenciador da tabela
        print("Inicializando o gerenciador da tabela...")
        table_manager = TableManager(client, spreadsheet_name="instagram", sheet_name="links")
        print("Gerenciador de tabela configurado com sucesso!")

        # Obter todos os links da tabela
        print("Lendo os links da tabela...")
        links = table_manager.get_links()
        print("Links encontrados:")
        for i, link in enumerate(links, start=1):
            print(f"{i}. {link}")

    except Exception as e:
        print(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    main()