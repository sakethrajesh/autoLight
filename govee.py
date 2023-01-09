import requests
import json
import enquiries
from config import govee_key

url = 'https://developer-api.govee.com/v1'
headers = {"content-type": "application/json", 'Govee-API-Key': govee_key }

devices = requests.get(url + '/devices', headers=headers)

print(devices.content)

options = ['on', 'off']
state = enquiries.choose('Choose one of these options: ', options)

payload = {
    'device':'e1:66:34:20:03:6d:62:62',
    'model':'H5081',
    'cmd': {
        'name': 'turn',
        'value': state
    }
}

plug = requests.put(url + '/devices/control', data=json.dumps(payload), headers=headers)

print(plug.content)
