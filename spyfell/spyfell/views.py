from django.shortcuts import render


def index(request):
    return render(request, 'spyfell/index.html', None)
