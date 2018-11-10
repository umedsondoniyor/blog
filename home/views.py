
from django.shortcuts import render, HttpResponse


def home_view(request):
    if request.user.is_authenticated():
        context = {
            'isim': 'Umedzhon'
        }
    else:
        context = {
            'isim': 'You are my guest'
        }
    return render(request, 'home.html', context)