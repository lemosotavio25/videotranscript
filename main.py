from instagram_download.downloader import download_instagram_video
from whisper_test.transcriber import transcribe_video
from goauth_service.gservice import authenticate_google_sheets
from table_manager.table import TableManager
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

                transcribe_video(video_path, "data/transcriptions", "pt")

                if video_path and text_path:

                    print(f"Vídeo salvo em: {video_path}")
                    print(f"Texto salvo em: {text_path}")

                processed_links.add(url)
            except Exception as e:
                print(f"Erro ao processar o link {url}: {e}")

    except Exception as e:
        print(f"Erro durante a execução: {e}")


