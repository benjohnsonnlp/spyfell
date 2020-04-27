import logging
import random

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Session, Player, Location

logger = logging.getLogger(__name__)


def get_image(location_name):
    search_url = "https://www.google.com/search?site=&tbm=isch&q={}".format(location_name)
    html = requests.get(search_url).text
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.select('td a img')[0].get('src')
    return image_url


def login(request):
    return render(request, 'game/createPlayer.html', None)


def save_player(request):
    name = request.POST['name']
    player, _ = Player.objects.get_or_create(name=name)

    logger.info('Logging in player {} with id {}'.format(name, player.id))
    player.save()
    return HttpResponseRedirect(reverse('session_list', args=[player.id]))


def session_list(request, player_id):
    sessions = Session.objects.order_by('created')
    context = {
        'sessions': sessions,
        'player': get_object_or_404(Player, pk=player_id),
    }
    return render(request, 'game/sessionList.html', context)


def session(request, player_id, session_id):
    session = get_object_or_404(Session, pk=session_id)
    players = list(session.player_set.all())
    active_player = get_object_or_404(Player, pk=player_id)
    active_player.active_session = session
    active_player.save()
    context = {
        "session": session,
        "active_player": active_player,
        "players": players
    }
    # if session.current_location:
    #     context['image_url'] = get_image(session.current_location.name)
    return render(request, 'game/session.html', context)


def create_session(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    session_name = request.POST['session_name']
    session = Session(name=session_name)
    session.save()
    return HttpResponseRedirect(reverse('session_details', args=[player.id, session.id]))


def save_location(request, player_id, session_id):
    active_player = get_object_or_404(Player, pk=player_id)

    location = Location.objects.create(name=request.POST['name'], created_by=active_player)
    location.save()
    logger.info('Creating location with name {} from player {} and id {}'.format(location.name,
                                                                                 location.created_by,
                                                                                 location.pk))

    session = get_object_or_404(Session, pk=session_id)
    session.current_location = location
    session.save()
    players = session.player_set.all()
    for candidate in players:
        candidate.is_spy = False
        candidate.save()

    culled_players = [p for p in players if p != active_player]
    for candidate in culled_players:
        if random.random() < (1 / len(players)) or candidate == culled_players[-1]:
            candidate.is_spy = True
            candidate.save()
            break

    return HttpResponseRedirect(reverse('session_details', args=(active_player.id, session.pk,)))


def remove_location(request, player_id, session_id):
    player = get_object_or_404(Player, pk=player_id)

    session = get_object_or_404(Session, pk=session_id)

    session.current_location = None
    session.save()
    return HttpResponseRedirect(reverse('session_details', args=(player.id, session.pk,)))


class SessionList(APIView):
    """
    List active sessions
    """

    def get(self, request, format=None):
        return Response(['1'])
