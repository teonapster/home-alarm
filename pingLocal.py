#author teonapster@gmail.com

import os

#Ping service constructed in order to check if a specific machine is active in local network
#If you use this service for authentication maybe its good idea to check mac address also :)
class PingLocal:
	
	def isActive(self,host):
		response = os.system("ping -c 1 -w 1 " + host+ " >/dev/null")
		
		#Host is active
		if response == 0:
			return True
		return False
