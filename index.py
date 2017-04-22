import requests
import os
token = os.environ.get('FB_ACCESS_TOKEN')
texte ='salut'
payload = {'recipient': {'id': '1285839391505940'}, 'message': {'text': texte}}
r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)

