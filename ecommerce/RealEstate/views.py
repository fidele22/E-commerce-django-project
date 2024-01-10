from django.shortcuts import render, redirect
from .forms import PhotoCardForm

# Create your views here.

from .models import PhotoCard

def index(request):
    cards = PhotoCard.objects.all()

    return render(request, 'pages/index.html', {'cards': cards})

