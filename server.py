from flask import Flask, render_template, request
from flask_socketio import SocketIO,  emit
from flask_restful import Api, Resource
# import RPi.GPIO as GPIO
import time




app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
api      = Api(app)


@app.route('/', methods=['GET'])
def timer():
    return render_template('timer.html')


@app.route('/timer/update', methods=['POST'])
def timer_update():
    new_time_seconds=request.get_json()['time']
    socketio.emit('timer_update', new_time_seconds)
    return 'ok', 200


alarm_pin=21

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(alarm_pin, GPIO.OUT)

alarm_is_on = False


current_time = lambda: int(round(time.time() *1000))

# Grant my..
last_request = 0
# and let me hold you..

class RaiseAlarmResource(Resource):
    def post(self):
        global alarm_is_on
        global last_request
        this_request = current_time()
        if alarm_is_on or (this_request-last_request < 5000):
            pass
        else:
            last_request = this_request

            # GPIO.output(alarm_pin, GPIO.LOW)
            alarm_is_on=True
        return 200

class LowerAlarmResource(Resource):
    def post(self):
        global alarm_is_on
        global last_request
        this_request = current_time()
        if not alarm_is_on or (this_request-last_request < 5000):
            pass
        else:
            last_request = this_request
            # GPIO.output(alarm_pin, GPIO.HIGH)
            alarm_is_on=False
        return 200

# GPIO.output(alarm_pin, GPIO.HIGH)

api.add_resource(RaiseAlarmResource, '/alarm/raise', endpoint='raise')
api.add_resource(LowerAlarmResource, '/alarm/lower', endpoint='lower')

# app.run(host='0.0.0.0')
