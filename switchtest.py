import RPi.GPIO as GPIO
#for the sleep method
import time

switch = 8

#set numbering mode for the program
GPIO.setmode(GPIO.BOARD)

#set switch(8) as output pin
GPIO.setup(switch, GPIO.OUT, initial = 0)

try:
	#turn cycle through hub modes at intervals of 1 second
	while(True):
		#turn on switch, set as HIGH or 1
		GPIO.output(switch, 1)
		print("ON")
		time.sleep(0.1)
		#turn off switch, set as LOW or 0
		GPIO.output(switch, 0)
		print("OFF")
		time.sleep(4.9)
except KeyboardInterrupt:
	#cleanup GPIO settings before exiting
	GPIO.cleanup()
	print("Exiting...")
