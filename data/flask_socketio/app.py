from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
# pip install flask flask_socketio eventlet

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Receiving Messages
@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

# @socketio.on('json')
# def handle_json(json):
#     print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)

def my_function_handler(data):
    print('received json: ' + str(json))
    return 'one', 2

socketio.on_event('my event', my_function_handler, namespace='/test')

# Sending Messages
@socketio.on('message')
def handle_messaage(message):
    send(message)

@socketio.on('json')
def handle_json(json):
    send(json, json=True)


# same as
'''
@socketio.on('my event', namespace='/json')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    return 'one', 2
'''

@app.route('/')
def index():
    return "For test"

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5000)