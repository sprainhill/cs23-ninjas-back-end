from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

@csrf_exempt
@api_view(["GET"])
def initialize(request):
    global rooms
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = Room.objects.all()
    room = player.room()
    sewer_rooms = Room.objects.filter(sewer=room.sewer)
    map = {
        "sewer": room.sewer,
        "rooms": [{
            'id': i.id,
            'x': i.x,
            'y': i.y,
            'n_to': i.n_to,
            's_to': i.s_to,
            'e_to': i.e_to,
            'w_to': i.w_to,
        } for i in sewer_rooms]
    }
    # rooms_visited = PlayerVisited.objects.filter(player=player)
    # visited_list = [i.room.id for i in rooms_visited]
    players = room.playerNames(player_id)

    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'room_id': room.id}, safe=True)


@csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
    elif direction == "s":
        nextRoomID = room.s_to
    elif direction == "e":
        nextRoomID = room.e_to
    elif direction == "w":
        nextRoomID = room.w_to
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom=nextRoomID
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        # for p_uuid in currentPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        # for p_uuid in nextPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'room_id': room.id, 'players':players, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'room_id': room.id, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    data = json.loads(request.body)
    player = request.user.player
    room = player.room()
    players_in_room = room.playerUUIDs(player.id)
    pusher.trigger(f'p-channel-{player.uuid}', u'broadcast',
                   {'message': f'You say "{data["message"]}"'})
    for p_uuid in players_in_room:
        pusher.trigger(f'p-channel-{p_uuid}', u'broadcast',
                       {'message': f'{player.user.username} says "{data["message"]}".'})
    return JsonResponse({'message': "It's Working, It's Working!"}, safe=True)


