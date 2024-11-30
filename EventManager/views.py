from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# from django.http import HttpResponseRedirect  
from .models import Event, Venue
from .models import EventDetail
from .forms import EventForm
from .models import Display

# Create your views here.
def home(request):
    all_events = Event.objects.all()
    return render(request, 'index.html',{
        'she':all_events
    })
    
def display(request):
    all_displays = Display.objects.all()
    return render(request, 'display.html',{
        'display': all_displays
    })


# def display(request, pk):
#     event = get_object_or_404(Event, pk=pk)
#     # If you're reversing the URL in the view
#     event_url = reverse('my_display', kwargs={'pk': event.pk})
#     return render(request, 'display.html', {'event': event, 'event_url': event_url})

# def event_detail(request, event_id):
#     all_event_details = EventDetail.objects.get(pk=event_id)
#     return render(request, 'EventManager/event_detail.html',{
#         'him':all_event_details
#     } )
# def event_detail(request, event_id):
#     print(f"Event ID passed: {event_id}")
#     event = get_object_or_404(Event, id=event_id)
#     event = Event.objects.get(pk=id)
#     event_detail = EventDetail.objects.get(event_name=event)
#     return render(request, 'EventManager/event_detail.html', {
#         'event': event,
#         'event_detail': event_detail,
#     })

def event_detail(request, event_id):
    events =  Event.objects.filter(pk=event_id)
    if events.exists():
        return render(request, 'EventManager/event_detail.html',{
            'events':events
        })
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