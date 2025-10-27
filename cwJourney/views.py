from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import LearningJourney, AboutMe

def index(request):
    journey = LearningJourney.objects.all()
    return render(request, 'index.html', {'journey': journey})

def about_me(request):
    me = AboutMe.objects.first()
    return render(request, 'aboutMe.html', {'me': me})
