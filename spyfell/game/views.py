import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Session, Player


def login(request):
    return render(request, 'game/createPlayer.html', None)


def save_player(request):
    name = request.POST['name']
    player = Player.objects.get(name=name)
    if not player:
        player = Player.objects.create(name=name)
    logging.info('Logging in player {} with id {}'.format(name, player.pk))
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
    player = get_object_or_404(Player, pk=request.GET['player'])
    player.active_session = session
    player.save()
    players = Player.objects.filter(active_session = session_id).select_related()
    return render(request, 'game/session.html', {"session": session, "players": players})


def create_session(request):
    return render(request, 'game/createSession.html', None)


def save_session(request):
    name = request.POST['name']
    session = Session.objects.create(name=name)
    logging.info('Creating session with name: {} and id {}'.format(name, session.pk))
    session.save()
    return HttpResponseRedirect(reverse('session_details', args=(session.pk,)))


class SessionList(APIView):
    """
    List active sessions
    """

    def get(self, request, format=None):
        return Response(['1'])
