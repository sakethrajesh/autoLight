from pyicloud import PyiCloudService
import getpass
from config import icloud_pass, govee_key
from math import radians, cos, sin, asin, sqrt
import datetime
import requests
import json
import asyncio
import socketio

sio = socketio.AsyncClient()

status = 0

@sio.on('statusChange')
async def statusChange(data):
    global status
    status = data['status']
    print('the lamp has been turned ' + str(status))

@sio.event
async def connect():
    print('****************connected********************')


@sio.event
async def disconnect():
    print('****************disconnected********************')



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

async def main():
    await sio.connect("http://127.0.0.1:8000")
    await sio.start_background_task(sstuff)

    # await sio.wait()
    # await sio.call('ping', {})

async def sstuff():
    # print('hello');

    while True:
        await sio.wait()
        print('hello');


async def stuff():
    # email = input('Email: ')
    # password = getpass.getpass("Password: ")

    api = PyiCloudService('sakethraj122@gmail.com', icloud_pass)

    global status

    print(api.data)

    now = datetime.datetime.now()
    # print('time now ' + str(now))
    five_pm = now.replace(hour=17, minute=0, second=0, microsecond=0)
    five_am = now.replace(hour=5, minute=0, second=0, microsecond=0)
    # print(now > five_pm)
    # print(now < five_am)


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

    while True:
        latitude = api.devices[3].location()['latitude']
        longitude = api.devices[3].location()['longitude']
        # print('coordinates: (' + str(latitude) + '', '' + str(longitude) + ')')
        # print(str(status))
        # distance = distance(lat1=37.24243167545431, lon1=-80.42904638540682, lat2=latitude, lon2=longitude)
        # print(distance(37.24243167545431, latitude, -80.42904638540682, longitude))
        # print('**************************************************************')


        if (now >= five_pm or now <= five_am) and distance(37.24243167545431, latitude, -80.42904638540682, longitude) <= 100:
            # print('in range and in time')

            if status == 0:
                payload = {
                    'device':'e1:66:34:20:03:6d:62:62',
                    'model':'H5081',
                    'cmd': {
                        'name': 'turn',
                        'value': 'on'
                    }
                }

                # print(requests.put(url + '/devices/control', data=json.dumps(payload), headers=headers).content)
                status = 1
            # else:
                # print('already on') 


        else:
            # print('not in range or not on time')

            if status == 1:
                payload = {
                    'device':'e1:66:34:20:03:6d:62:62',
                    'model':'H5081',
                    'cmd': {
                        'name': 'turn',
                        'value': 'off'
                    }
                }

                # print(requests.put(url + '/devices/control', data=json.dumps(payload), headers=headers).content)
                status = 0
            # else:
                # print('already off') 





asyncio.run(main())

