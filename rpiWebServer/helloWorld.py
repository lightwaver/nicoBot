from flask import Flask, render_template
import RPi.GPIO as GPIO
import datetime

import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil1_A_1_pin = 22 # pink
coil1_A_2_pin = 27 # orange
coil1_B_1_pin = 17 # blau
coil1_B_2_pin = 4 # gelb

coil2_A_1_pin = 6  # 26 # pink
coil2_A_2_pin = 13 # 19 # orange
coil2_B_1_pin = 19 # 13 # blau
coil2_B_2_pin = 26 # 6 # gelb

GPIO.setup(coil1_A_1_pin, GPIO.OUT)
GPIO.setup(coil1_A_2_pin, GPIO.OUT)
GPIO.setup(coil1_B_1_pin, GPIO.OUT)
GPIO.setup(coil1_B_2_pin, GPIO.OUT)

GPIO.setup(coil2_A_1_pin, GPIO.OUT)
GPIO.setup(coil2_A_2_pin, GPIO.OUT)
GPIO.setup(coil2_B_1_pin, GPIO.OUT)
GPIO.setup(coil2_B_2_pin, GPIO.OUT)

# anpassen, falls andere Sequenz
# StepCount = 8
# Seq = list(range(0, StepCount))
# Seq[0] = [0,1,0,0]
# Seq[1] = [0,1,0,1]
# Seq[2] = [0,0,0,1]
# Seq[3] = [1,0,0,1]
# Seq[4] = [1,0,0,0]
# Seq[5] = [1,0,1,0]
# Seq[6] = [0,0,1,0]
# Seq[7] = [0,1,1,0]

StepCount = 4
Seq = list(range(0, StepCount))
Seq[0] = [1,1,0,0]
Seq[1] = [0,1,1,0]
Seq[2] = [0,0,1,1]
Seq[3] = [1,0,0,1]


def setStep1(w1, w2, w3, w4):
    GPIO.output(coil1_A_1_pin, w1)
    GPIO.output(coil1_A_2_pin, w2)
    GPIO.output(coil1_B_1_pin, w3)
    GPIO.output(coil1_B_2_pin, w4)

def setStep2(w1, w2, w3, w4):
    GPIO.output(coil2_A_1_pin, w1)
    GPIO.output(coil2_A_2_pin, w2)
    GPIO.output(coil2_B_1_pin, w3)
    GPIO.output(coil2_B_2_pin, w4)

stepper1 = 0
stepper2 = 0

delay = 0.2;
setStep1(0,0,0,0);
setStep2(0,0,0,0);
time.sleep(delay);

setStep1(1,0,0,0);
setStep2(1,0,0,0);
time.sleep(delay);

setStep1(0,1,0,0);
setStep2(0,1,0,0);
time.sleep(delay);

setStep1(0,0,1,0);
setStep2(0,0,1,0);
time.sleep(delay);

setStep1(0,0,0,1);
setStep2(0,0,0,1);
time.sleep(delay);

setStep1(0,0,0,0);
setStep2(0,0,0,0);
time.sleep(delay);


def straight(delay, steps, direction):
    for i in range(steps):
        for j in range(StepCount):
            global stepper1, stepper2
            stepper1 = (stepper1 + direction) % StepCount;
            stepper2 = (stepper2 + direction) % StepCount;

            setStep1(Seq[stepper1][0], Seq[stepper1][1], Seq[stepper1][2], Seq[stepper1][3])
            setStep2(Seq[stepper2][0], Seq[stepper2][1], Seq[stepper2][2], Seq[stepper2][3])
            time.sleep(delay)


def rotate(delay, steps, direction = 1):
    for i in range(steps):
        for j in range(StepCount):
            global stepper1
            global stepper2
            stepper1 = (stepper1 + direction) % StepCount;
            stepper2 = (stepper2 - direction) % StepCount;

            setStep1(Seq[stepper1][0], Seq[stepper1][1], Seq[stepper1][2], Seq[stepper1][3])
            setStep2(Seq[stepper2][0], Seq[stepper2][1], Seq[stepper2][2], Seq[stepper2][3])
            time.sleep(delay)

if __name__ == '__main__':
#    while True:
        try:
            delay = 20 #18; #raw_input("Zeitverzoegerung (ms)?")
            steps = 64 * 2; #raw_input("Wie viele Schritte vorwaerts? ")
            print ('forward')
            straight(int(delay) / 10000.0, int(steps), -1)
            print ('back')
            straight(int(delay) / 10000.0, int(steps), 1)

            print ('right')
            rotate(int(delay) / 10000.0, int(steps), 1)
            print ('left')
            rotate(int(delay) / 10000.0, int(steps), -1)
        finally:
            setStep1(0,0,0,0);
            setStep2(0,0,0,0);

# app = Flask(__name__)
# @app.route("/")
# def hello():
#    now = datetime.datetime.now()
#    timeString = now.strftime("%Y-%m-%d %H:%M")
#    templateData = {
#       'title' : 'Hallo Nico!',
#       'time': timeString
#       }
#    return render_template('index.html', **templateData)

# if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=80, debug=True)