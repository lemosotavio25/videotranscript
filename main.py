from instagram_download.downloader import download_instagram_video
from whisper_test.transcriber import transcribe_video
from goauth_service.gservice import authenticate_google_sheets
from table_manager.table import TableManager
from open_ai_assistant.assistant import OpenAIChatAssistant
import os

if __name__ == "__main__":
    try:
        client = authenticate_google_sheets()
        table_manager = TableManager(client, spreadsheet_name="instagram", sheet_name="links")
        links = table_manager.get_links()

        processed_links = set()  # Para evitar duplicatas

        for url in links:
            if url in processed_links:
                print(f"Link já processado: {url}")
                continue

            try:
                print(f"Processando o link: {url}")
                video_path, text_path = download_instagram_video(url)

                output_file = transcribe_video(video_path, "data/transcriptions", "pt")

                if video_path and text_path:
                    try:
                        with open(text_path, "r", encoding="utf-8") as file:
                            text_content = file.read()

                        with open(output_file, "r", encoding="utf-8") as file:
                            output_text = file.read()

                        print("Conteúdo do arquivo lido com sucesso:")
                        print(text_content)
                        print(output_text)

                        # Processar o texto com o assistente
                        assistant = OpenAIChatAssistant()
                        response = assistant.get_response(text_content + output_text)

                        print("Resposta do assistente:")
                        print(response)

                    except FileNotFoundError:
                        print(f"Erro: O arquivo {text_path} não foi encontrado.")
                    except Exception as e:
                        print(f"Erro ao processar o texto: {e}")

            except Exception as e:
                print(f"Erro ao processar o link {url}: {e}")

    except Exception as e:
        print(f"Erro durante a execução: {e}")


