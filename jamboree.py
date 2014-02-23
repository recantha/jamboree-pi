#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from random import choice

# Set-up GPIO and clear
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)

# Define GPIO pins
PINS=[17,18,27,22,23,24,25,4,10]
for PIN in PINS:
	GPIO.setup(PIN, GPIO.OUT)

# Define number of cycles of each pattern
flash_cycles = 3
cylon_cycles = 5
master_pulse_cycles = 0
pulse_cycles = 1
colour_cycles = 5
line_cycles = 5
random_cycles = 50
pairs_cycles = 8

# Define speeds for each pattern
flash_speed = 0.2
cylon_speed = 0.05
pulse_speed = 0.002
colour_speed = 0.2
line_speed = 0.5
random_speed = 0.1
pairs_speed = 0.06

while True:
	for i in range(flash_cycles):
		for PIN in PINS:
			GPIO.output(PIN, GPIO.HIGH)

		time.sleep(flash_speed)

		for PIN in PINS:
			GPIO.output(PIN, GPIO.LOW)

		time.sleep(flash_speed)

	for cylon_cycle in range(cylon_cycles):
		GPIO.output(17, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(18, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(18, GPIO.LOW)
		GPIO.output(22, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(24, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(25, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(25, GPIO.LOW)
		GPIO.output(10, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(4, GPIO.LOW)
		time.sleep(cylon_speed)
		GPIO.output(10, GPIO.LOW)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(4, GPIO.LOW)
		GPIO.output(25, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(4, GPIO.LOW)
		GPIO.output(24, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(25, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(22, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(27, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(18, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(17, GPIO.HIGH)
		time.sleep(cylon_speed)
		GPIO.output(18, GPIO.LOW)
	GPIO.output(17, GPIO.LOW)

	for mp in range(master_pulse_cycles):
		for PIN in PINS:
			p = GPIO.PWM(PIN,50)
			p.start(0)
			for pulse in range(pulse_cycles):
				for i in range(100):
					p.ChangeDutyCycle(100-i)
					time.sleep(pulse_speed)
	
				for i in range(100):
					p.ChangeDutyCycle(0+i)
					time.sleep(pulse_speed)
			p.stop()

	for colour_cycle in range(colour_cycles):
		GPIO.output(27, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(10, GPIO.LOW)
		GPIO.output(17, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		time.sleep(colour_speed)

		GPIO.output(17, GPIO.LOW)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(23, GPIO.HIGH)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(colour_speed)

		GPIO.output(18, GPIO.LOW)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(4, GPIO.LOW)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(10, GPIO.HIGH)
		time.sleep(colour_speed)

	for i in range(line_cycles):
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)
		GPIO.output(10, GPIO.LOW)
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(4, GPIO.HIGH)

		time.sleep(line_speed)

		GPIO.output(17, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(23, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(10, GPIO.HIGH)
		GPIO.output(18, GPIO.LOW)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(4, GPIO.LOW)

		time.sleep(line_speed)

	for i in range(random_cycles):
		first = choice(PINS)
		second = choice(PINS)
		GPIO.output(first, GPIO.HIGH)
		GPIO.output(second, GPIO.HIGH)
		time.sleep(random_speed)
		GPIO.output(first, GPIO.LOW)
		GPIO.output(second, GPIO.LOW)

	for i in range(pairs_cycles):
		GPIO.output(17, GPIO.HIGH)
		GPIO.output(18, GPIO.HIGH)
		time.sleep(pairs_speed)
		GPIO.output(17, GPIO.LOW)
		GPIO.output(18, GPIO.LOW)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		time.sleep(pairs_speed)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		time.sleep(pairs_speed)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(pairs_speed)
		GPIO.output(25, GPIO.LOW)
		GPIO.output(4, GPIO.LOW)
		GPIO.output(10, GPIO.HIGH)
		time.sleep(pairs_speed)
		GPIO.output(10, GPIO.LOW)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(pairs_speed)
		GPIO.output(25, GPIO.LOW)
		GPIO.output(4, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		time.sleep(pairs_speed)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		time.sleep(pairs_speed)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(22, GPIO.LOW)
