from socketIO_client import SocketIO

with SocketIO('localhost', 5000) as socketIO:
    # socketIO.emit('message', 'good')
    # socketIO.wait_for_callbacks(seconds=1)
    data = {'username': 'jehyeon', 'room': 'goodbye'}
    # Requires logic update to bring room list
    socketIO.emit('join',data)