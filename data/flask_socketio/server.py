from flask import Flask, render_template
from flask_socketio import SocketIO, join_room #, session 

from Room import Room

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Receiving Message
@socketio.on('message')
def handle_message(message):
    print('receive message: ' + message)
    # return "success"

# Room
@socketio.on('join')
def on_join(data):
    # If the user first connects, it is the same as the room name
    username = data['username']
    room = data['room']

    if not Room.IsExists(room):
        Room(username)
    else:
        Room.find(room).join(username)

    join_room(room)

    socketio.emit('in', {'data': username + ' entered the ' + room}, room=room)
    print('[noti] ' + username + ' entered the ' + room)
    # room argument cause the message to be sent to all the clients that are in given room.

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']

    Room.find(room).leave(username)

    leave_room(room)
    socketio.send(username + ' has left the room.', room=room)
    print('[noti] ' + username + ' has left the ' + room)

@socketio.on('getInfo')
def getInfo(room):
    data = {}
    socketio.emit(data,room=room)
    pass

@socketio.on('updateInfo')
def updateInfo(data):
    '''

    '''
    pass

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5000)