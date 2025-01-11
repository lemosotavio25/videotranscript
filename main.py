from instagram_download.downloader import download_instagram_video
from whisper_test.transcriber import transcribe_video
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


# Exemplo de uso
if __name__ == "__main__":
    # URL do vídeo do Instagram
    instagram_url = "https://www.instagram.com/"

    # Executar a função principal
    try:
        download_and_transcribe(instagram_url)
    except Exception as e:
        print(f"Erro no processo: {e}")
