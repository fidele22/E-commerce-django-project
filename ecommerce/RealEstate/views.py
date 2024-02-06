from django.shortcuts import render, redirect
from .models import PhotoCard

def index(request):
    cards = PhotoCard.objects.all()

    return render(request, 'pages/index.html', {'cards': cards})

def account(request):

    return render(request, 'pages/account.html')
