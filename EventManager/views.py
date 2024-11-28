from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect  
from .models import Event, Venue
from .models import EventDetail
from .forms import EventForm

# Create your views here.
def home(request):
    all_events = Event.objects.all()
    return render(request, 'index.html',{
        'she':all_events
    })
def event_detail(request, event_id):
    all_event_details = EventDetail.objects.get(pk=event_id)
    return render(request, 'EventManager/event_detail.html',{
        'him':all_event_details
    } )
    
def add_event(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/add_event?submitted=True')
    else:
            form = EventForm
            if 'submitted' in request.GET:
                submitted = True
                
                
    return render(request, 'EventManager/add_event.html',{
                    'form':form, 'submitted':submitted
    })
def list_venues(request):
    all_venues = Venue.objects.all()
    return render(request, 'EventManager/list_venues.html',{
        'them':all_venues
    })
def show_venue(request, venue_id):
    venue =  Venue.objects.get(pk=venue_id)
    return render(request, 'EventManager/show_venue.html',{
        'it':venue
    })