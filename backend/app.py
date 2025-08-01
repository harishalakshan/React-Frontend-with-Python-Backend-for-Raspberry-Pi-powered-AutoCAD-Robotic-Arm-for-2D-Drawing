
from flask import Flask, request
from flask_cors import CORS
import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
SERVO_X, SERVO_Y = 17, 18
GPIO.setup(SERVO_X, GPIO.OUT)
GPIO.setup(SERVO_Y, GPIO.OUT)
pwm_x = GPIO.PWM(SERVO_X, 50)
pwm_y = GPIO.PWM(SERVO_Y, 50)
pwm_x.start(7.5)
pwm_y.start(7.5)

def move_servo(pwm, angle):
    duty = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)

def inverse_kinematics(x, y, L1=10, L2=10):
    cos_angle2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    angle2 = math.acos(cos_angle2)
    angle1 = math.atan2(y, x) - math.atan2(L2 * math.sin(angle2), L1 + L2 * math.cos(angle2))
    return math.degrees(angle1), math.degrees(angle2)

app = Flask(__name__)
CORS(app)

@app.route('/api/draw', methods=['POST'])
def draw():
    data = request.get_json()
    for coord in data['coordinates']:
        x_angle = coord['x']
        y_angle = coord['y']
        move_servo(pwm_x, x_angle)
        move_servo(pwm_y, y_angle)
    return {"status": "Drawing executed"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
