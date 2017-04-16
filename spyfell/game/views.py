from django.shortcuts import render, get_object_or_404
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


class SessionList(APIView):
    '''
    List active sessions
    '''

    def get(self, request, format=None):
        return Response(['1'])