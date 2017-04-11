#author teonapster@gmail.com
import RPi.GPIO as io
from isensor import ISensor

#DoorSwitch class enables magnetic sensor (connected through gpio port)
class DoorSensor(ISensor):
	
	#sensor initialization
	def __init__(self,pin,name):
		ISensor.__init__(self)
		io.setmode(io.BCM)
		io.setup(pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp		
		self.setPin(pin)
		self.setName(name)
		print ("Instantiate switch "+name+" (pin: "+str(self.pin)+")")
	
	#ISensor override get sensor value active/inactive
	def getValue(self):
		print ("Check "+self.name)
		isOpen = io.input(self.pin)
		if isOpen:
			print (self.name+" is open!!!")
		return isOpen
	
	#ISensor override (prints msg)
	def getAlarmMsg(self):
		if io.input(self.pin):
			return self.name+" is open!!!\n"
		return ""
