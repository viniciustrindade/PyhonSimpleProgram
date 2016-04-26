# -*- coding: utf-8 -*-
from MusicStore import MusicStore

class TestMusicStore:
	def main(self):
		musicStore = MusicStore()
		musicStore.setOwner("Roberto")
		print musicStore.toString()