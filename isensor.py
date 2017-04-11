#author teonapster@gmail.com
from abc import ABCMeta, abstractmethod

class ISensor:
	__metaclass__ = ABCMeta
	
	def setPin(self,pin):
		self.pin = pin
	
	def setName(self,name):
		self.name = name

	def getPin(self):
		return self.pin
	
	@abstractmethod
	def getValue(self): raise NotImplementedError
	
	@abstractmethod
	def getAlarmMsg(): raise NotImplementedError
