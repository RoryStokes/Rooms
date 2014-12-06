from player import Player
from copy import copy
import random

class Game:
	def __init__(self):
		self.players = []
		self.started = False

	def addPlayer(self,name):
		id = len(self.players)
		self.players.append(Player(name,id))
		return id

	def player(self,id):
		return self.players[id]

	def setTargets(self):
		order = copy(self.players)
		random.shuffle(order)
		for i in range(len(order)):
			j = (i+1)%len(order)
			order[i].target = order[j]