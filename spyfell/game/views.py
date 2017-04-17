import logging
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Session


def index(request):
    sessions = Session.objects.order_by('name')
    context = {
        'sessions': sessions
    }
    return render(request, 'game/index.html', context)


def session(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    return render(request, 'game/session.html', {"session": session})


def create_session(request):
    return render(request, 'game/createSession.html', None)


def save_session(request):
    name = request.POST['name']
    logging.info('Creating session with name: {}'.format(name))
    session = Session.objects.create(name=name)
    print('Id is {}'.format(session.pk))
    session.save()
    return HttpResponseRedirect(reverse('session_details', args=(session.pk,)))


class SessionList(APIView):
    """
    List active sessions
    """

    def get(self, request, format=None):
        return Response(['1'])
