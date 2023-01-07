import requests
import json

url = 'https://developer-api.govee.com/v1'
headers = {"content-type": "application/json", 'Govee-API-Key': 'a1cc86f4-4677-42c6-b2c9-5d405d8997a5' }

devices = requests.get(url + '/devices', headers=headers)

print(devices.content)

# r = requests.put(url, data=json.dumps(payload), headers=headers)


payload = {
    'device':'e1:66:34:20:03:6d:62:62',
    'model':'H5081',
    'cmd': {
        'name': 'turn',
        'value': 'on'
    }
}

plug = requests.put(url + '/devices/control', data=json.dumps(payload), headers=headers)

print(plug.content)
