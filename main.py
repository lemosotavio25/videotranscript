from instagram_download.downloader import download_instagram_video
from whisper_test.transcriber import transcribe_video
from goauth_service.gservice import authenticate_google_sheets
from table_manager.table import TableManager
import os

def download_and_transcribe(instagram_url, download_folder="data/downloads", transcription_folder="data/transcriptions"):
    """ 
    Baixa um vídeo do Instagram e transcreve o áudio/vídeo.

    :param instagram_url: URL do vídeo no Instagram.
    :param download_folder: Diretório onde o vídeo será salvo.
    :param transcription_folder: Diretório onde a transcrição será salva.
    """
    # Garantir que os diretórios existem
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    if not os.path.exists(transcription_folder):
        os.makedirs(transcription_folder)

    # Baixar o vídeo do Instagram
    print("Baixando o vídeo do Instagram...")
    download_instagram_video(instagram_url, download_folder)

    # Identificar o arquivo de vídeo baixado
    video_file = None
    for file in os.listdir(download_folder):
        if file.endswith(".mp4"):  # Procura por arquivos MP4
            video_file = os.path.join(download_folder, file)
            break

    if not video_file:
        raise FileNotFoundError("Nenhum arquivo de vídeo encontrado no diretório de downloads.")

    # Caminho para o arquivo de transcrição
    transcription_file = os.path.join(
        transcription_folder, os.path.splitext(os.path.basename(video_file))[0] + "_transcription.txt"
    )

    # Transcrever o vídeo
    print("Transcrevendo o áudio/vídeo...")
    transcribe_video(video_file, transcription_file, language="pt")

    print("Processo concluído com sucesso!")


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
                download_instagram_video(url)
                processed_links.add(url)
            except Exception as e:
                print(f"Erro ao processar o link {url}: {e}")

    except Exception as e:
        print(f"Erro durante a execução: {e}")

        #um pequeno erro, a transcricao foi feita apenas duas vezes
        #OpenAI ApI -> renomear transcription e resumir junto 
