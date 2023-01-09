from pyicloud import PyiCloudService
import getpass

email = input('Email: ')
password = getpass.getpass("Password: ")

api = PyiCloudService('sakethraj122@gmail.com', password)

print(api.data)

off = 0;

while off < 100:
    latitude = api.devices[3].location()['latitude']
    longitude = api.devices[3].location()['longitude']
    print('coordinates: (' + str(latitude) + '', '' + str(longitude) + ')')

    print('**************************************************************')

    off += 1

    # if input('end service (yes/no): ') == 'yes':
    #     off = True



