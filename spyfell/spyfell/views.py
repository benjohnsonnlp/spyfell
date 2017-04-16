from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return render(request, 'spyfell/index.html', None)


class SessionList(APIView):
    '''
    List active sessions
    '''
    def get(self, request, format=None):
        return Response(['1'])