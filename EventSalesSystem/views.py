from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {})

def pages_blank(request):
    return render(request, 'pages/blank.html', {})

def pages_contact(request):
    return render(request, 'pages/contact.html', {})

def pages_error_404(request):
    return render(request, 'pages/error_404.html', {})

def pages_faq(request):
    return render(request, 'pages/faq.html', {})

def pages_login(request):
    return render(request, 'pages/login.html', {})

def pages_register(request):
    return render(request, 'pages/register.html', {})

def pages_general(request):
    return render(request, 'pages/general.html', {})

def pages_profile(request):
    return render(request, 'pages/profile.html', {})
