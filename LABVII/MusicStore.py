# -*- coding: utf-8 -*-
class MusicStore:
	def __init__(self):
		self.owner = "sem dono."
	def setOwner(self,owner):
		self.owner = owner
	def displayHoursOfOperation(self):
		print "\n Perído: Diariamente das 9:00 AM - 21:00 PM"
		print "\n %s, Propietário" %self.owner