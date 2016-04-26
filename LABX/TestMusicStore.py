# -*- coding: utf-8 -*-
from MusicStore import MusicStore

class TestMusicStore:
	def main(self):
		musicStore = MusicStore()
		musicStore.setOwner("Roberto")
		titles = []
		titles.append({"titulo": "A Festa", "artista": "Ivete Sangalo"})
		titles.append({"titulo": "Luna Nueva", "artista": "Diego Torres"})
		musicStore.setTitles(titles)
		musicStore.displayMusicTitles()