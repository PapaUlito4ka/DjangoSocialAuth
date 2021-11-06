import requests
from social_app.settings import SECRET_KEY

BASE = 'http://localhost:8000/api/messages/'
HEADERS = {
    'token': SECRET_KEY
}


def get_last_message():
    url = BASE + 'last'
    res = requests.get(url, headers=HEADERS)
    return res.json()['data']


def send_message(text: str, user_id: int):
    url = BASE + 'send'
    data = {
        'text': text,
        'user_id': user_id
    }
    res = requests.post(url, headers=HEADERS, data=data)
    return {
        'status_code': res.status_code,
        **res.json()
    }