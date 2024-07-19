import RPi.GPIO as GPIO
from time import sleep

'''
Purpose: Increase/Decrease Voltage with enough energy to burn the burnwire. 
'''

GPIO.setmode(GPIO.BCM)
port_num=26
GPIO.setup(port_num,GPIO.OUT)
burn_seconds=4

GPIO.output(port_num,GPIO.HIGH)
sleep(burn_seconds)
GPIO.output(port_num,GPIO.LOW)
