from pyicloud import PyiCloudService
import getpass
from config import icloud_pass, govee_key
from math import radians, cos, sin, asin, sqrt
import datetime
import requests
import json
import enquiries

def distance(lat1, lat2, lon1, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = c*20925721.784777
      
    # calculate the result
    return r

email = input('Email: ')
password = getpass.getpass("Password: ")

api = PyiCloudService('sakethraj122@gmail.com', icloud_pass)

print(api.data)

now = datetime.datetime.now()
print('time now ' + str(now))
six_pm = now.replace(hour=18, minute=0, second=0, microsecond=0)
six_am = now.replace(hour=6, minute=0, second=0, microsecond=0)
print(now > six_pm)
print(now < six_am)


url = 'https://developer-api.govee.com/v1'
headers = {"content-type": "application/json", 'Govee-API-Key': govee_key }
payload = {
    'device':'e1:66:34:20:03:6d:62:62',
    'model':'H5081',
    'cmd': {
        'name': 'turn',
        'value': 'off'
    }
}
requests.put(url + '/devices/control', data=json.dumps(payload), headers=headers)
status = False
off = 0;

while True:
    latitude = api.devices[3].location()['latitude']
    longitude = api.devices[3].location()['longitude']
    print('coordinates: (' + str(latitude) + '', '' + str(longitude) + ')')

    # distance = distance(lat1=37.24243167545431, lon1=-80.42904638540682, lat2=latitude, lon2=longitude)
    print(distance(37.24243167545431, latitude, -80.42904638540682, longitude))
    print('**************************************************************')

    off += 1

    # 

    if (now >= six_pm or now <= six_am) and distance(37.24243167545431, latitude, -80.42904638540682, longitude) <= 100:
        print('in range')

        if not status:
            payload = {
                'device':'e1:66:34:20:03:6d:62:62',
                'model':'H5081',
                'cmd': {
                    'name': 'turn',
                    'value': 'on'
                }
            }

            print(requests.put(url + '/devices/control', data=json.dumps(payload), headers=headers).content)
            status = True
        else:
            print('already on') 


    else:
        print('not in range')

        if status:
            payload = {
                'device':'e1:66:34:20:03:6d:62:62',
                'model':'H5081',
                'cmd': {
                    'name': 'turn',
                    'value': 'off'
                }
            }

            print(requests.put(url + '/devices/control', data=json.dumps(payload), headers=headers).content)
            status = False
        else:
            print('already off') 


    # if input('end service (yes/no): ') == 'yes':
    #     off = True



