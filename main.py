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
    r = 3956*5280
      
    # calculate the result
    return(c * r)

email = input('Email: ')
password = getpass.getpass("Password: ")

api = PyiCloudService('sakethraj122@gmail.com', icloud_pass)

print(api.data)

now = datetime.datetime.now()
print('time now ' + str(now))
six_pm = now.replace(hour=18, minute=0, second=0, microsecond=0)
print(now > six_pm)

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
print(requests.put(url + '/devices/control', data=json.dumps(payload), headers=headers).content)
status = False
off = 0;

while off < 100:
    latitude = api.devices[3].location()['latitude']
    longitude = api.devices[3].location()['longitude']
    # print('coordinates: (' + str(latitude) + '', '' + str(longitude) + ')')

    print('**************************************************************')

    off += 1

    if now <= six_pm and distance(lat1=latitude, lon1=longitude, lat2=37.683441657148066, lon2=-120.94261014871186) <= 8:
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

    # if input('end service (yes/no): ') == 'yes':
    #     off = True



