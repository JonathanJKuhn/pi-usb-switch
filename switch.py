import RPi.GPIO as GPIO
import db
import time

current_port = db.current_port
port_name = db.port_name
switch = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch, GPIO.OUT, initial = 0)

#Ask user to select input and display current input. Then convert input to int
print("Current Port")
print(f'{current_port} - {port_name[current_port]}')
value = input("Please select a port (1-4)\n")
value = int(value)

#Switch input based on the number of steps required, then run update_current function
def change_port(steps):
	for x in range(0, steps):
		GPIO.output(switch, 1)
		time.sleep(0.1)
		GPIO.output(switch, 0)
		time.sleep(0.1)
	GPIO.cleanup()
	update_current(value)

#Update current port value within db.py
def update_current(value):
	f = open('./db.py', 'r')
	data = f.readlines()
	f.close()
	data[0] = f'current_port = {value}\n'
	f = open('./db.py', 'w')
	f.writelines(data)
	f.close()

#Compare current_inpt to value
if value > current_port:
	steps = value - current_port
elif value < current_port:
	if current_port == 4:
		steps = value
	elif current_port == 3:
		steps = value + 1
	else:
		steps = 3
else:
	steps = 0
	
#Start change_inpt based on steps
change_port(steps)

#Display results
print(f'Port changed to {value} - {port_name[value]}')
