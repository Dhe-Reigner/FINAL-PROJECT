from django.shortcuts import render
from .models import Event
from .models import EventDetail

# Create your views here.
def home(request):
    all_events = Event.objects.all()
    return render(request, 'index.html',{
        'she':all_events
    })
def event_detail(request):
    all_event_details = EventDetail.objects.all()
    return render(request, 'event_detail.html',{
        'him':all_event_details
    } )