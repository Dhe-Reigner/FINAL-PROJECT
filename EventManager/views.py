from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from .models import Event, Venue
from .models import EventDetail
from .forms import EventForm
from .models import Display
from .models import Kid
from .models import Lifestyle
from .models import Movie




# Create your views here.
def home(request):
    all_events = Event.objects.all()
    return render(request, 'index.html',{
        'she':all_events
    })
def stk(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0742957112'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        
        return HttpResponse("STK Push in Django👋")

def display(request):
    all_displays = Display.objects.all()
    return render(request, 'display.html',{
        'display': all_displays
    })
# def display(request, event_id):
#     all_displays =  Event.objects.filter(pk=event_id)
#     if all_displays.exists():
#         return render(request, 'EventManager/display.html',{
#             'all_displays':all_displays
#         })


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



    
def kids(request):
    all_kids =  Kid.objects.all()
    return render(request, 'kids.html',{
            'all_kids':all_kids
        })
def lifestyle(request):
    all_lifestyle =  Lifestyle.objects.all()
    return render(request, 'lifestyle.html',{
            'all_lifestyle':all_lifestyle
        })
        
def movies(request):
    all_movies =  Movie.objects.all()
    return render(request, 'movies.html',{
            'all_movies':all_movies
        })
# from django.shortcuts import render, redirect, reverse
# from django.conf import settings

# from FinalProject.mixins import Directions
# '''Basic view for routing'''

# def route(request):
#     context = {
#         'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
#         'GOOGLE_MAPS_URL': settings.GOOGLE_MAPS_URL,
#         'base_country':settings.BASE_COUNTRY
#     }
#     return render(request, 'EventManager/route.html', context)


# '''Basic view for displaying a map'''
# def map(request):
#     lat_a = request.GET('lat_a',None)
#     long_a = request.GET('long_a',None)
#     lat_b = request.GET('lat_b',None)
#     long_b = request.GET('long_b',None)
#     lat_c = request.GET('lat_c',None)
#     long_c = request.GET('long_c',None)
#     lat_d = request.GET('lat_d',None)
#     long_d = request.GET('long_d',None)

#     #only call API if all 4 addresses are added
#     # if lat_a and lat_b and lat_c and lat_d:
#     #     directions = Directions(
#     #         origin=(lat_a, long_a),
#     #         destination=(lat_b, long_b),
#     #         waypoints=[(lat_c, long_c), (lat_d, long_d)],
#     #         api_key=settings.GOOGLE_MAPS_API_KEY
#     #     )
#     #     context = {
#     #         'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
#     #         'GOOGLE_MAPS_URL': settings.GOOGLE_MAPS_URL,
#     #         'directions': directions
#     #     }
#     #     return render(request, 'EventManager/map.html', context)
#     # else:
#     #     return redirect(reverse('route'))

#     #only call API if all 4 addresses are added
#     if lat_a and lat_b and lat_c and lat_d:
#        directions = Directions(
#            lat_a, lat_a,
#            long_a, long_a,
#            lat_b, lat_b,
#            long_b, long_b,
#            lat_c, lat_c,
#            long_c, long_c,
#            lat_d, lat_d,
#            long_d, long_d,

#        )
#     else:
#         return redirect(reverse('main:route'))

#     context = {
#         "google_api_key":settings.GOOGLE_API_KEY,
#         "base_country": settings.BASE_COUNTRY,
#         "lat_a":lat_a,
#         "long_a":long_a,
#         "lat_b":lat_b,
#         "long_b":long_b,
#         "lat_c":lat_c,
#         "long_c":long_c,
#         "lat_d":lat_d,
#         "long_d":long_d,
#         "origin":f'{lat_a},{long_a}',
#         "destination":f'{lat_b},{long_b}',
#         "waypoints": f'{lat_c},{long_c},{lat_d},{long_d}',  # comma-separated list of waypoints
#         "directions": directions,
#     }
#     return render(request, 'EventManager/map.html', context)