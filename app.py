from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate-idea', methods=['POST'])
def generate_idea():
    user_input = request.json.get('input')

    headers = {
        'Authorization': f"Bearer {os.getenv('OPENAI_API_KEY')}",
        'Content-Type': 'application/json',
    }
    
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': user_input}],
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)

    if response.status_code == 200:
        idea = response.json()['choices'][0]['message']['content']
        print(response.text)
        return jsonify({'idea': idea})
    else:
        print(response.text)
        return jsonify({'error': 'Erro ao gerar ideia'}), 500

if __name__ == '__main__':
    app.run(debug=True)
