from pyicloud import PyiCloudService

email = input('Email: ')
password = input("Password: ")

api = PyiCloudService('sakethraj122@gmail.com', 'Sakvith27')

print(api.devices[3].location())

# off = False

off = 0;

while off < 100:
    latitude = api.devices[3].location()['latitude']
    longitude = api.devices[3].location()['longitude']
    print('coordinates: (' + str(latitude) + '', '' + str(longitude) + ')')

    print('**************************************************************')

    off += 1

    # if input('end service (yes/no): ') == 'yes':
    #     off = True



