import openai
from open_ai_assistant.api_key import API_KEY

class OpenAIChatAssistant:
    """
    Classe para interagir com a API OpenAI ChatCompletion.
    """
    def __init__(self, api_key=API_KEY, model="gpt-4o-mini"):
        """
        Inicializa o assistente com a chave da API e o modelo.

        :param api_key: Chave da API OpenAI.
        :param model: Modelo a ser utilizado (padrão: "gpt-4").
        """
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def get_response(self, prompt, system_message=None):
        """
        Envia uma mensagem ao modelo OpenAI e retorna a resposta.

        :param prompt: A mensagem enviada ao modelo.
        :param system_message: Uma mensagem de sistema opcional para definir o contexto.
        :return: A resposta gerada pelo modelo.
        """
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message.content.strip()
        except openai.error.OpenAIError as e:
            print(f"Erro ao se comunicar com a API OpenAI: {e}")
            return None