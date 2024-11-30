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
    '''Used to append url parameters when redirecting users'''
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
    
    
