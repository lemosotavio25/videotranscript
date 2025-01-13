import os
import instaloader

def download_instagram_video(instagram_url, target_folder="data/downloads"):
    """
    Baixa um vídeo do Instagram, renomeia-o para video_N.mp4 e retorna o caminho do arquivo.

    :param instagram_url: URL do vídeo no Instagram.
    :param target_folder: Diretório onde os arquivos serão salvos.
    :return: Caminho completo do arquivo .mp4 baixado.
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
        save_metadata=False  # Não salvar metadados
    )

    try:
        # Antes do download: lista de arquivos existentes
        existing_files = set(os.listdir(target_folder))

        # Baixar o post
        print(f"Baixando o vídeo de: {instagram_url}")
        post = instaloader.Post.from_shortcode(loader.context, instagram_url.split("/")[-2])
        loader.download_post(post, target=target_folder)

        # Após o download: lista de arquivos novos
        new_files = set(os.listdir(target_folder)) - existing_files
        video_file = None
        text_file = None

        # Identificar os novos arquivos baixados
        for filename in new_files:
            if filename.endswith(".mp4"):
                video_file = os.path.join(target_folder, filename)
            elif filename.endswith(".txt"):
                text_file = os.path.join(target_folder, filename)

        # Garantir que ambos os arquivos foram encontrados
        if not video_file or not text_file:
            raise FileNotFoundError("Os arquivos de vídeo ou texto não foram encontrados após o download.")

        # Renomear os arquivos
        video_count = len([f for f in os.listdir(target_folder) if f.startswith("video_") and f.endswith(".mp4")]) + 1
        new_video_name = f"video_{video_count}.mp4"
        new_text_name = f"video_{video_count}.txt"

        new_video_path = os.path.join(target_folder, new_video_name)
        new_text_path = os.path.join(target_folder, new_text_name)

        os.rename(video_file, new_video_path)
        os.rename(text_file, new_text_path)

        print(f"Vídeo renomeado para: {new_video_path}")
        print(f"Texto renomeado para: {new_text_path}")

        return new_video_path, new_text_path

    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")
        return None, None