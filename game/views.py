import logging
import random

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Session, Player, Location

logger = logging.getLogger(__name__)


def login(request):
    return render(request, 'game/createPlayer.html', None)


def save_player(request):
    name = request.POST['name']
    player = None
    try:
        player = Player.objects.get(name=name)
    except:
        pass
    if not player:
        player = Player.objects.create(name=name)
    logger.info('Logging in player {} with id {}'.format(name, player.pk))
    player.save()
    return HttpResponseRedirect(reverse('session_list') + "?player={}".format(player.pk))


def session_list(request):
    sessions = Session.objects.order_by('created')
    player_id = request.GET['player']
    context = {
        'sessions': sessions,
        'playerId': player_id,
    }
    return render(request, 'game/sessionList.html', context)


def session(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    players = Player.objects.filter(active_session=session_id).select_related()
    active_player = get_object_or_404(Player, pk=request.GET['player'])
    active_player.active_session = session
    active_player.save()
    return render(request, 'game/session.html', {"session": session, "active_player": active_player, "players": players})


def create_session(request):
    player = get_object_or_404(Player, pk=request.GET['player'])
    return render(request, 'game/createSession.html', {'player': player})


def save_session(request):
    player = get_object_or_404(Player, pk=request.POST['player_id'])
    name = request.POST['name']
    session = Session.objects.create(name=name)
    logger.info('Creating session with name: {} and id {}'.format(name, session.pk))
    session.save()
    return HttpResponseRedirect(reverse('session_details', args=(session.pk,)) + "?player={}".format(player.pk))


def save_location(request):
    active_player = get_object_or_404(Player, pk=request.POST['player_id'])

    location = Location.objects.create(name=request.POST['name'], created_by=active_player)
    location.save()
    logger.info('Creating location with name {} from player {} and id {}'.format(location.name,
                                                                                  location.created_by,
                                                                                  location.pk))

    session = get_object_or_404(Session, pk=request.POST['session'])
    session.current_location = location
    session.save()
    players = Player.objects.filter(active_session=session.pk).select_related()
    for candidate in players:
        candidate.is_spy = False
        candidate.save()

    culled_players = [p for p in players if p != active_player]
    for candidate in culled_players:
        if random.random() < (1 / len(players)) or candidate == culled_players[-1]:
            candidate.is_spy = True
            candidate.save()
            break

    return HttpResponseRedirect(reverse('session_details', args=(session.pk,)) + "?player={}".format(active_player.pk))


def remove_location(request):
    player = get_object_or_404(Player, pk=request.POST['player_id'])

    session = get_object_or_404(Session, pk=request.POST['session'])
    session.current_location = None
    session.save()
    return HttpResponseRedirect(reverse('session_details', args=(session.pk,)) + "?player={}".format(player.pk))


class SessionList(APIView):
    """
    List active sessions
    """

    def get(self, request, format=None):
        return Response(['1'])
