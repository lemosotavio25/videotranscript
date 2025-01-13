class TableManager:
    """
    Classe para lidar com a tabela do Google Sheets.
    Focada na planilha 'instagram', na aba de links (primeira coluna).
    """
    def __init__(self, client, spreadsheet_name="instagram", sheet_name="links"):
        """
        Inicializa o gerenciador da tabela.
        
        :param client: Cliente gspread autenticado.
        :param spreadsheet_name: Nome da planilha principal.
        :param sheet_name: Nome da aba dentro da planilha.
        """
        self.client = client
        self.spreadsheet_name = spreadsheet_name
        self.sheet_name = sheet_name
        self.sheet = None
        self._load_sheet()

    def _load_sheet(self):
        """
        Carrega a planilha e a aba especificada.
        """
        try:
            print(f"Abrindo a planilha '{self.spreadsheet_name}'...")
            spreadsheet = self.client.open(self.spreadsheet_name)
            self.sheet = spreadsheet.worksheet(self.sheet_name)
            print(f"Aba '{self.sheet_name}' carregada com sucesso!")
        except Exception as e:
            print(f"Erro ao carregar a aba '{self.sheet_name}': {e}")
            raise

    def get_links(self):
        """
        Obtém todos os links da primeira coluna (ignorando o cabeçalho).
        
        :return: Lista de links.
        """
        try:
            print("Lendo os links da primeira coluna...")
            links = self.sheet.col_values(1)[1:]  # Ignora o cabeçalho
            print(f"Links encontrados: {len(links)}")
            return links
        except Exception as e:
            print(f"Erro ao obter os links: {e}")
            raise

    def add_link(self, link):
        """
        Adiciona um novo link à primeira coluna.
        
        :param link: Link a ser adicionado.
        """
        try:
            print(f"Adicionando o link: {link}")
            next_row = len(self.sheet.col_values(1)) + 1
            self.sheet.update_cell(next_row, 1, link)
            print("Link adicionado com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar o link: {e}")
            raise

    def update_link(self, row, new_link):
        """
        Atualiza um link existente em uma linha específica.
        
        :param row: Número da linha a ser atualizada.
        :param new_link: Novo link a ser inserido.
        """
        try:
            print(f"Atualizando o link na linha {row}: {new_link}")
            self.sheet.update_cell(row, 1, new_link)
            print("Link atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar o link: {e}")
            raise