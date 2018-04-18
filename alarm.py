from flask import Flask
from flask_restful import Api, Resource
import RPi.GPIO as GPIO

app = Flask(__name__)
api = Api(app)

alarm_pin=21

GPIO.setmode(GPIO.BCM)
GPIO.setup(alarm_pin, GPIO.OUT)

class RaiseAlarmResource(Resource):
    def post(self):
        GPIO.output(alarm_pin, GPIO.LOW)
        return 200

class LowerAlarmResource(Resource):
    def post(self):
        GPIO.output(alarm_pin, GPIO.HIGH)
        return 200

GPIO.output(alarm_pin, GPIO.HIGH)
        
api.add_resource(RaiseAlarmResource, '/alarm/raise', endpoint='raise')
api.add_resource(LowerAlarmResource, '/alarm/lower', endpoint='lower')

app.run(host='0.0.0.0')
