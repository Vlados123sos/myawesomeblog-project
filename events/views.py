from django.shortcuts import render
from .models import Event
# Create your views here.
def home(requst):
    events=Event.objects
    return render(requst ,'events/home.html',{'events':events})