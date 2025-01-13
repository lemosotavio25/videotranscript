import whisper
import os

import os
import whisper

def transcribe_video(input_file, output_dir="data/transcriptions", language="pt", max_length=123):
    """
    Transcreve um vídeo ou áudio e salva a transcrição formatada em um arquivo.

    :param input_file: Caminho para o arquivo de entrada (vídeo/áudio).
    :param output_dir: Diretório onde será salva a transcrição.
    :param language: Idioma para transcrição (padrão: "pt").
    :param max_length: Máximo de caracteres por linha na transcrição.
    """
    # Verificar se o arquivo de entrada existe
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {input_file}")

    # Garantir que o diretório de saída exista
    os.makedirs(output_dir, exist_ok=True)

    # Gerar o nome do arquivo de saída com base no arquivo de entrada
    base_name = os.path.basename(input_file)  # Extrai o nome do arquivo
    base_name_no_ext = os.path.splitext(base_name)[0]  # Remove a extensão
    output_file = os.path.join(output_dir, f"{base_name_no_ext}_transcription.txt")

    # Carregar o modelo
    print("Carregando o modelo Whisper...")
    model = whisper.load_model("small")

    # Transcrever o áudio/vídeo
    print("Transcrevendo o áudio...")
    result = model.transcribe(input_file, language=language)

    # Texto transcrito
    transcription = result['text']

    # Quebrar o texto em linhas de no máximo max_length caracteres
    lines = []
    for word in transcription.split():
        if not lines or len(lines[-1]) + len(word) + 1 > max_length:
            lines.append(word)
        else:
            lines[-1] += " " + word

    # Salvar a transcrição formatada no arquivo de saída
    with open(output_file, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line.strip() + "\n")

    print(f"Transcrição salva em: {output_file}")
    return output_file

