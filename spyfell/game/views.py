from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Session


def index(request):
    sessions = Session.objects.order_by('name')
    context = {
        'sessions': sessions
    }
    return render(request, 'game/index.html', context)


class SessionList(APIView):
    '''
    List active sessions
    '''

    def get(self, request, format=None):
        return Response(['1'])
