import whisper
import os

def transcribe_video(input_file, output_file, language="pt", max_length=123):
    """
    Transcreve um vídeo ou áudio e salva a transcrição formatada em um arquivo.

    :param input_file: Caminho para o arquivo de entrada (vídeo/áudio).
    :param output_file: Caminho para o arquivo onde será salva a transcrição.
    :param language: Idioma para transcrição (padrão: "pt").
    :param max_length: Máximo de caracteres por linha na transcrição.
    """
    # Verificar se o arquivo de entrada existe
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {input_file}")

    # Carregar o modelo
    print("Carregando o modelo Whisper...")
    model = whisper.load_model("small")

    # Transcrever o áudio/vídeo
    print("Transcrevendo o áudio...")
    result = model.transcribe(input_file, language=language)

    # Texto transcrito
    transcription = result['text']

    # Quebrar o texto em linhas de no máximo max_length caracteres
    lines = [transcription[i:i+max_length] for i in range(0, len(transcription), max_length)]

    # Salvar a transcrição formatada no arquivo de saída
    with open(output_file, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line.strip() + "\n")  # Remove espaços extras e adiciona quebra de linha

    print(f"Transcrição salva em: {output_file}")
