# coding:utf-8

import RPi.GPIO as GPIO
import time

Led = 14
TRIG = 2
ECHO = 3


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Led, GPIO.OUT)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def blink_by_frequency(duration, frequency):
    num_of_loops = duration*frequency
    interval = 1/frequency/2
    for i in list(range(int(num_of_loops))):
        GPIO.output(Led, True)
        time.sleep(interval)
        GPIO.output(Led, False)
        time.sleep(interval)
    return

def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO) == False:
        pass
    time_start = time.time()
    while GPIO.input(ECHO) == True:
        pass
    time_end = time.time()

    pulse_duration = time_end- time_start
    distance = pulse_duration * 340 * 100 * 0.5
    distance = round(distance,2)
    print('current distance is {} cm'.format(distance))
    return distance

print('press Enter to start measuring distances...')
try:
    while True:
        distance_cm = int(measure_distance())
        input_frequency = max(2, 16-distance_cm)
#        if distance_cm > 15:
#            input_frequency = 2
#        else:
#            input_frequency = 16-distance_cm
        blink_by_frequency(0.5, input_frequency)
        #time.sleep(0.5)
except:
    print('bye')
    GPIO.cleanup()

