# -*- coding: utf-8 -*-
import time
from MusicTitle import MusicTitle

class MusicStore:
	def __init__(self):
		self.owner = "sem dono."
		self.openTime = 9
		self.closeTime = 21
		self.titles = []
	def setOwner(self,owner):
		self.owner = owner
	def setOpen(self,open):
		self.openTime = open
	def geOpen(self):
		return self.openTime
	def setClose(self,close):
		self.closeTime = close
	def geClose(self):
		return self.closeTime
	def isOpen(self):
		return self.getHourInt() >= self.openTime and self.getHourInt() <= self.closeTime
	def getOpenClosedMessage(self):
		if self.isOpen():
			return " Estamos abertos!!"
		else:
			return " Estamos fechados!!"
	def displayHoursOfOperation(self):
		print "\n Perído: Diariamente das %s:00 AM - %s:00 PM" %(self.openTime,self.closeTime)
		print "\n"+ self.getOpenClosedMessage()
		print "\n %s, Propietário" %self.owner
	def getHourInt(self):
		return time.localtime(time.time()).tm_hour
	def setTitles(self,titles):
		self.titles = titles
	def getTitles(self):
		return self.titles
	def displayMusicTitles(self):
		count = 0
		for t in self.titles:
			count += 1
			print "Título %i" %count
			print " Título:" + t["titulo"]
			print " Artista:" + t["artista"]

	def toString(self):
		return { "Dono":self.owner,"Abre":self.openTime,"Fecha" : self.closeTime}