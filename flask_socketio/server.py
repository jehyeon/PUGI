from flask import Flask, render_template
from flask_socketio import SocketIO, join_room #, session 

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# update room 
# def Room:
#     DATA = {'number_of_room' : 0, 'room_list' : []}

#     def __init__(room_name):



# def join(room):
#     if room in Info:
#         return 
#     else:
#         Info[room].
#     join_room(room)

# Receiving Message
@socketio.on('message')
def handle_message(message):
    print('receive message: ' + message)
    return "success"

'''
# More to check
@socketio.on('my event', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('received json: ' + str(json))
    return 'one', 2
'''

# Need log 

# Room
@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']

    join_room(room)

    # Update Info
    # Info[]
    socketio.emit('in', {'data': username + ' entered the ' + room}, room=room)
    print('[noti] ' + username + ' entered the ' + room)
    # room argument cause the message to be sent to all the clients that are in given room.

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    socketio.send(username + ' has left the room.', room=room)

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