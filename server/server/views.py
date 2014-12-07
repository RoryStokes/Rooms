from django.http import HttpResponse, HttpResponseRedirect
from player import Player
from game import Game
import json

def connect(request):
	global game
	if game.started:
		return HttpResponse('[{"messages": ["Error: the game has already started."], "moveIDs": [], "moveNames": []}]')
	if request.method == 'GET':
		id = game.addPlayer(request.GET['name'])

		while not game.started:
			pass

		player = game.player(id)
		response = {"id": id, "cop": player.cop, "currentRoom": player.currentRoom['name'], "moveIDs": player.currentRoom['connected'],
		 "moveNames": [ game.map['rooms'][i]['name'] for i in player.currentRoom['connected'] ] }
		messages = []
		messages.append("The game has started.")
		messages.append("You are in the "+player.currentRoom['name']+".")

		if player.cop:
			messages.append("You are the cop.")
		else:
			messages.append("Your target is "+player.target.name+".")
			messages.append(game.cop.name + " is the cop.")
			response["target"] = player.target.name

		for line in othersInRoom(game,player):
			messages.append(line)

		response["messages"] = messages

		return HttpResponse(json.dumps([response]))
	return HttpResponse("")

def othersInRoom(game,player):
	for other in game.players:
		if other != player:
			yield(other.name + " is in the room with you.")

def action(request):
	global game
	if not game.started:
		return HttpResponse('[{"messages": "Error: the game has not yet started.", "moveIDs": [], "moveNames": []}]')
	if request.method == 'GET':
		id = request.GET['id']
		action = request.GET['action']

		while not game.started:
			pass

		player = game.player(id)
		response = {"id": id, "cop": player.cop, "currentRoom": player.currentRoom['name'], "moveIDs": player.currentRoom['connected'],
		 "moveNames": [ game.map['rooms'][i]['name'] for i in player.currentRoom['connected'] ] }
		messages = []
		messages.append("The game has started.")
		messages.append("You are in the "+player.currentRoom['name']+".")

		if player.cop:
			messages.append("You are the cop")
		else:
			messages.append("Your target is "+player.target.name+".")
			messages.append(game.cop.name + " is the cop.")
			response["target"] = player.target.name

		for other in game.players:
			if other != player:
				messages.append(other.name + " is in the room with you.")

		response["messages"] = messages

		return HttpResponse(json.dumps([response]))
	return HttpResponse("")

def init(request):
	global game
	game = Game()
	return HttpResponse("Ready to connect")

def start(request):
	global game
	if len(game.players) > 2:
		game.setTargets()
		game.loadMap('test')
		game.started = True
		return HttpResponseRedirect('game')

	return HttpResponse("Not enough players")

def game(request):
	return HttpResponse("GAMELEL")

def state(request):
	global q
	print q
	while q == 'not':
		pass
	return HttpResponse(q)