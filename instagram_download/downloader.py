import instaloader
import os


def download_instagram_video(instagram_url, target_folder="data/downloads"):
    """
    Baixa um vídeo do Instagram e salva apenas o arquivo de vídeo (.mp4) e o arquivo de texto (.txt).

    :param instagram_url: URL do vídeo no Instagram.
    :param target_folder: Diretório onde os arquivos serão salvos.
    """
    # Garantir que o diretório de destino exista
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Inicializar o instaloader com configurações personalizadas
    loader = instaloader.Instaloader(
        download_pictures=False,  # Não baixar imagens (.jpg)
        download_video_thumbnails=False,  # Não baixar thumbnails
        download_comments=False,  # Não baixar comentários
        compress_json=False,  # Não salvar arquivos .json.xz
        dirname_pattern=target_folder,  # Salvar na pasta especificada
        filename_pattern="{date_utc}",  # Nome base do arquivo baseado na data UTC
        save_metadata=False

    )

    try:
        # Extrair o shortcode da URL
        shortcode = instagram_url.split("/")[-2]

        # Baixar o post
        print(f"Baixando o vídeo de: {instagram_url}")
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=".")

        # Verificar e mover os arquivos necessários para o target_folder
        for filename in os.listdir("."):
            if filename.endswith(".mp4") or filename.endswith(".txt"):
                os.rename(filename, os.path.join(target_folder, filename))
            else:
                # Remover arquivos indesejados (caso ainda sejam criados)
                os.remove(filename)

        print(f"Download concluído! Arquivos salvos em: {target_folder}")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")
