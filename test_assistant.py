from open_ai_assistant.assistant import OpenAIChatAssistant

assistant = OpenAIChatAssistant()
response = assistant.get_response("Say this is a test")
print(response)