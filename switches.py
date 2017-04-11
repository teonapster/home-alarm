#author teonapster@gmail.com
import time
from mailer import MailSender
from pingLocal import PingLocal
from doorSensor import DoorSensor
from pirSensor import PirSensor

#mail sender
x = MailSender()

#Ping service
y = PingLocal()

#Construct some door swithces
doorSwitches = [ DoorSensor(22,"side door"),DoorSensor(27,"main door")]

#Construct a pir sensor
pirSensor = PirSensor(17,"main room sensor")

#Normally disabled alarm state
alarmOn = False

while True:

	#Authentication host (remember to use leased local ip address or refactor method to support mac address)
	isAnybodyHere = y.isActive("192.168.1.2")

	
	if not isAnybodyHere:
		print ("Boss is out")
	
	#get current state from sensors
	door1 = doorSwitches[0].getValue()
	door2 = doorSwitches[1].getValue()
	pirSensor1 = pirSensor.getValue()
	
	#any door is open?
	switch = door1 or door2
	print (switch)
	
	if switch or pirSensor1 and not alarmOn == True: #if any sensor is active (e.g door is open, or pir detected motion) and alarm is not already enabled
		if not isAnybodyHere: #if your authentication device is out
			print("ALARM!")
			alarmOn = True
			x.sendMail("teonapster@gmail.com","ALARM!!!",doorSwitches[0].getAlarmMsg()+doorSwitches[1].getAlarmMsg()+pirSensor.getAlarmMsg()) #send mail (Remember to add your address here!
			print("Mail sent to teonapster")
		else:
			print("Motion detected but the boss is here") #Motion detected but authentication device is inhouse
			alarmOn = False #disable alarm
	elif alarmOn == True:
		alarmOn = False
		print("Alarm disabled")
	time.sleep(0.5) #check sensor state every 0.5 second
