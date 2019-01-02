from socketIO_client import SocketIO

def response(args):
    print('server - ' + args['data'])

def getUsername():
    return 'jehyeon'

# temp
done = False
with SocketIO('localhost', 5000) as socketIO:
    com = input()
    # socketIO.emit('message', 'good')
    # socketIO.wait_for_callbacks(seconds=1)
    data = {'username': getUsername(), 'room': 'goodbye'}
    # Requires logic update to bring room list
    socketIO.emit('join',data)
    socketIO.on('in', response)
    socketIO.wait(seconds=1)