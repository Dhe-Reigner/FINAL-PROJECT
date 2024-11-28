from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect  
from .models import Event
from .models import EventDetail
from .forms import EventForm

# Create your views here.
def home(request):
    all_events = Event.objects.all()
    return render(request, 'index.html',{
        'she':all_events
    })
def event_detail(request):
    all_event_details = EventDetail.objects.all()
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