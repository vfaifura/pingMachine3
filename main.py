import requests as requests
from json import dumps
from httplib2 import Http
import time
from datetime import datetime

connectionStatus = ""
def webHook(connectionStatus):
    """Hangouts Chat incoming webhook."""
    url = 'https://chat.googleapis.com/v1/spaces/AAAA76hEQeY/messages?key=' \
          'AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=' \
          'vHjHhLP_PN7DB50US9McENEVoF1ra4PSxLhzUzaDgXU%3D'

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    text = "*Time*: " + current_time + "\n*Network status*: " + connectionStatus
    bot_message = {
        'text': text
    }
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)


while(True):
    def checkConnection():
        x = requests.get('https://b3ca-93-77-254-210.eu.ngrok.io')
       # print(x.status_code)
        if x.status_code == 502:
            connectionStatus = "ONLINE"
            return connectionStatus
        else:
            connectionStatus = "DOWN"
            return connectionStatus
    webHook(checkConnection())
    time.sleep(300)