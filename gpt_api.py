# 1  Получить ТОКЕН
# 2  Написать запрос к API и получить ответ
# 3  Отправить ответ в чат

import requests
TOKEN = ''

def ask_gpt(question):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN}'
    }
    body = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }
    response = requests.post(url, json=body, headers=headers)
    data =  response.json()
    return data['choices'][0]['message']['content']