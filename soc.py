import socketio

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    print(sid, 'connected')

@sio.event
async def disconnect(sid):
    print(sid, 'disconnected')

@sio.event
async def on(sid, data):
    result = data['status']
    print('the lamp has been turned ' + str(result))
    await sio.emit('statusChange', {'status':1})

@sio.event
async def off(sid, data):
    result = data['status']
    print('the lamp has been turned ' + str(result))
    await sio.emit('statusChange', {'status':0})

@sio.event
async def ping(sid, data):
    print('hii')

