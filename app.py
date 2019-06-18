from gevent import monkey
from flask import Flask, render_template
from flask_socketio import SocketIO

import redis

monkey.patch_all()

app = Flask(__name__)

db = redis.StrictRedis('localhost', 6379, 0)
socketio = SocketIO(app)


@app.route('/')
def main():
    return render_template('main.html')


@socketio.on('connect', namespace='/socketio')
def ws_conn():
    c = db.incr('user_count')
    socketio.emit('msg', {'count': c}, namespace='/socketio')


@socketio.on('disconnect', namespace='/socketio')
def ws_disconn():
    c = db.decr('user_count')
    socketio.emit('msg', {'count': c}, namespace='/socketio')


@socketio.on('text', namespace='/socketio')
def ws_city(message):
    socketio.emit('text', {'text': message['text']}, namespace='/socketio')

if __name__ == '__main__':
    socketio.run(app)
