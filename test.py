from flask import Flask
import request

app = Flask(name)

Beget_API_URL = 'https://api.beget.com/api/mailbox/ #указываю урл почты


def create_email(mailbox):
    api_key = 'my_api_key'
    url= f'{Beget_API_URL}/mailbox/add'
    params= {
        'login' : 'mailbox'
        'password' : 'mailbox_password'
    }
    response = requests.post(Beget_API_URL + 'add', params=params)
    return response.json()

    if response == 'create':
        return f'Email {mailbox}@mydomain.com sozdan'
    else:
        return 'FALL'

def delete_email(mailbox):
    api_key = 'my_api_key'
    url= f'{Beget_API_URL}/mailbox/delete'
    params= {
        'login' : 'mailbox'
        'password' : 'mailbox_password'
    }
    response = requests.post(Beget_API_URL + 'delete', params=params)
    return response.json()

    if response == 'delete':
        return f'Email {mailbox}@mydomain.com ydalen'
    else:
        return 'FALL'

if name == 'main':
    app.run(port=5555)

# Создание почтового ящика с помощью запроса через сurl
curl -X POST http://localhost:5555/create/my_mailbox_name

# Удаление почтового ящика
curl -X POST http://localhost:5555/delete/my_mailbox_name
