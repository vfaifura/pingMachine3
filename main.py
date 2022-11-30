import psutil
import requests as requests
from json import dumps
from httplib2 import Http
import time
from datetime import datetime

connectionStatus = ""
def webHook(connectionStatus):
    """Hangouts Chat incoming webhook."""
    url = 'https://chat.googleapis.com/v1/spaces/AAAA8b3pdq0/messages?key=' \
          'AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=' \
          'Qa0BGbauWvK9lJiNaTIINPebdKngqvltIqYivjBN7nw%3D'

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    text = "Time: " + current_time + "\n *Network status*: " + connectionStatus
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
        x = requests.get('https://cd55-188-163-32-2.ngrok.io/')
       # print(x.status_code)
        if x.status_code == 502:
            connectionStatus = "ON :)"
            return connectionStatus
        else:
            connectionStatus = "DOWN -_- "
            return connectionStatus
    webHook(checkConnection())
    time.sleep(300)