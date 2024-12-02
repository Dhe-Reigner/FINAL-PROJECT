from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {})

def pages_blank(request):
    return render(request, 'pages_blank.html', {})

def pages_contact(request):
    return render(request, 'pages_contact.html', {})

def pages_error_404(request):
    return render(request, 'pages_error_404.html', {})

def pages_faq(request):
    return render(request, 'pages_faq.html', {})

def pages_login(request):
    return render(request, 'pages_login.html', {})

def pages_register(request):
    return render(request, 'pages_register.html', {})

def pages_general(request):
    return render(request, 'pages_general.html', {})

def pages_profile(request):
    return render(request, 'pages_profile.html', {})

def affiliate_marketing(request):
    return render(request, 'affiliate_marketing.html', {})

def content_marketing(request):
    return render(request, 'content_marketing.html', {})

def email_marketing(request):
    return render(request, 'email_marketing.html', {})

def influencer_marketing(request):
    return render(request, 'influencer_marketing.html', {})

def mobile_marketing(request):
    return render(request, 'mobile_marketing.html', {})

def social_media_marketing(request):
    return render(request, 'social_media_marketing.html', {})

def video_marketing(request):
    return render(request, 'video_marketing.html', {})