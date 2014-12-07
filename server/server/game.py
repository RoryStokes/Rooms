from player import Player
from copy import copy
import random
import json

class Game:
	def __init__(self):
		self.players = []
		self.started = False

	def addPlayer(self,name):
		id = len(self.players)
		self.players.append(Player(name,id))
		return id

	def loadMap(self,name):
		self.map = json.load(open('../buildings/'+name+'.json'))
		for player in self.players:
			player.currentRoom = self.map['rooms'][0]

	def player(self,id):
		return self.players[id]

	def setTargets(self):
		order = copy(self.players)
		random.shuffle(order)
		order[0].cop = True
		self.cop = order[0]
		for i in range(1,len(order)):
			order[i].cop = False
			j = (i+1)
			if j >= len(order):
				j = 1
			order[i].target = order[j]