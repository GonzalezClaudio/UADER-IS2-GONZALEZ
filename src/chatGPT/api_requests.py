import requests
from config import API_KEY, ORGANIZACION # Importacion de config.py


def get_models():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "OpenAI-Organization": ORGANIZACION
    }
    response = requests.get("https://api.openai.com/v1/models", headers=headers)
    return response.json()

def chat_completo(query):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
        "OpenAI-Organization": ORGANIZACION
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"You: {query}"}],
        "temperature": 0.7
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    return response.json()
