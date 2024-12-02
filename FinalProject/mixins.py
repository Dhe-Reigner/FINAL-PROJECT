from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
import json
import datetime
from humanfriendly import format_timespan
from django.http import JsonResponse

# def FormErrors(*args):
#     errors = []
#     for arg in args:
#         if isinstance(arg, dict):
#             errors.extend(FormErrors(**arg))
#         elif isinstance(arg, list):
#             errors.extend(FormErrors(*arg))
#         elif isinstance(arg, str):
#             errors.append(arg)
#     return errors

def FormError(*args):
    message = ""
    for f in args:
        if f.errors:
            message = f.errors.as_text()
    return message

# def reCAPTCHAValidation(token):
#     url = "https://www.google.com/recaptcha/api/siteverify"
#     params = {
#         "secret": settings.RECAPTCHA_SECRET_KEY,
#         "response": token,
#         "remoteip": settings.CLIENT_IP_ADDRESS
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     if not data["success"]:
#         return False
#     return True

def reCAPTCHAValidation(request):
    '''reCAPTCHA validation'''
    result = requests.post(
        'https://www.google.com/recaptcha/api/siteverify', 
        data={
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': token
        })
    return result.json()

def RedirectParams(**kwargs):
    '''Used to append url parameters when redirecting members'''
    url = kwargs.get('url')
    params = kwargs.get('params', {})
    response = redirect(url)
    if params:
        query_string = urlencode(params)
        response['Location'] += '?' + query_string
        return response
    
class AjaxFormMixin(object):
    '''Mixin to ajaxify django form - can be over written in view by calling'''
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            message = FormErrors(form)
            return JsonResponse({'result':'Error', 'message':message})
        return response
    
    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            form.save()
            message = "Form submitted successfully"
            return JsonResponse({'result':'Success', 'message':""})
        return response
    
    
def Directions(*args, **kwargs):
    '''Handles directions from Google'''
    lat_a = kwargs.get("lat_a")
    long_a = kwargs.get("long_a")
    lat_b = kwargs.get("lat_b")
    long_b = kwargs.get("long_b")
    lat_c = kwargs.get("lat_c")
    long_c = kwargs.get("long_c")
    lat_d = kwargs.get("lat_d")
    long_d = kwargs.get("long_d")
    
    origin = f"{lat_a},{long_a}"
    destination = f"{lat_b},{long_b}"
    waypoints = f"{lat_c},{long_c}|{lat_d},{long_d}"
    
    # response = requests.get(url)
    # url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&waypoints={waypoints}&key={api_key}"
    # api_key = settings.GOOGLE_MAPS_API_KEY

    result = requests.get(
        'https://maps.googleapis.com/maps/api/directions/json?',
        params={
            'origin': origin,
            'destination': destination,
            'waypoints': waypoints,
            'key': settings.GOOGLE_MAPS_API_KEY
    })
    directions = result.json()
    
    if directions["status"] == "OK":
        
        routes = directions["routes"][0]["legs"]
        
        distance = 0
        duration = 0
        route_list = []
        
        for route in range(len(routes)):
            
            distance += int(routes[route]["distance"]["value"])
            duration += int(routes[route]["duration"]["value"])
            
            route_step  ={
                'origin':routes[route]["start_address"],
                'destination':routes[route]["end_address"],
                'distance': routes[route]["distance"]["text"],
                'duration': routes[route]["duration"]["text"], 
                
                'steps':[
                    [
                    a["distance"]["text"],
                    a["duration"]["text"],
                    a["html_instructions"], 
                ]
                for a in routes[route]["steps"]]
            }
            
    return {
        "origin":origin,
        "destination":destination,
        "distance": f"{round(distance/1000, 2)} Km",
        "duration": format_timespan(duration),
        "route": route_list,
        "status": directions["status"]
    }