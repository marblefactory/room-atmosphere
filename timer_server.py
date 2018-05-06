from flask import Flask, render_template, request
from flask_socketio import SocketIO,  emit




app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def timer():
    return render_template('timer.html')


@app.route('/timer/update', methods=['POST'])
def timer_update():
    new_time_seconds=request.get_json()['time']
    socketio.emit('timer_update', new_time_seconds)
    return 'ok', 200
