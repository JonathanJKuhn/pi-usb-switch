import RPi.GPIO as GPIO
import subprocess
import time

switch = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch, GPIO.OUT, initial = 0)
GPIO.setwarnings(False)

	
for i in range(0,4):
	#Check if USB switch is connected to RPi
	usb_list = subprocess.check_output("lsusb").decode('utf-8')
	if '0bda:5411' in usb_list:
		#If true, cleanup python, print sucess, and exit the application
		GPIO.cleanup()
		#Update current port value within db.py
		f = open('db.py', 'r')
		data = f.readlines()
		f.close()
		data[0] = f'current_port = 2\n'
		f = open('db.py', 'w')
		f.writelines(data)
		f.close()
		print('USB Switch is calibrated.')
		break
	#Cycle to the next port and continue through loop
	GPIO.output(switch, 1)
	time.sleep(0.1)
	GPIO.output(switch, 0)
	time.sleep(5)
