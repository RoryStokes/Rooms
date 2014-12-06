from django.http import HttpResponse, HttpResponseRedirect
from player import Player
from game import Game
import json

def connect(request):
	global game
	if game.started:
		return HttpResponse("Game has started")
	if request.method == 'GET':
		id = game.addPlayer(request.GET['name'])

		while not game.started:
			pass

		response = {"id": id, "target": game.player(id).target.name}
		return HttpResponse(json.dumps([response]))
	return HttpResponse("")

def init(request):
	global game
	game = Game()
	return HttpResponse("Ready to connect")

def start(request):
	global game
	if len(game.players) > 1:
		game.setTargets()
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