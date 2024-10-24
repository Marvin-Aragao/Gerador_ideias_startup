import requests
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    'Authorization': f"Bearer {os.getenv('OPENAI_API_KEY')}",
    'Content-Type': 'application/json',
}

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [{'role': 'user', 'content': 'Dê uma ideia de startup.'}],
}

response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
print(response.json())
