from django.shortcuts import render
from .models import Social
from.models import Content
from.models import Email
from.models import Influencer
from.models import Affiliate
from.models import Video
from.models import Mobile



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

def top_selling(request):
    return render(request, 'top_selling.html', {})

def affiliate_marketing(request):
    all_affiliate = Affiliate.objects.all()
    return render(request, 'affiliate_marketing.html', {
        'all_affiliate': all_affiliate,  # pass all affiliate marketing data to the template,  # pass all social media data to the template
    })

def content_marketing(request):
    all_content = Content.objects.all()
    return render(request, 'content_marketing.html', {
        'all_content': all_content,  # pass all content marketing data to the template,  # pass all social media data to the template
    })

def email_marketing(request):
    all_email = Email.objects.all()
    return render(request, 'email_marketing.html', {
        'all_email': all_email,  # pass all email marketing data to the template,  # pass all social media data to the template
    })

def influencer_marketing(request):
    all_influencer = Influencer.objects.all()
    return render(request, 'social_media_marketing.html', {
        'all_influencer': all_influencer,  # pass all influencer data to the template
    })

def mobile_marketing(request):
    all_mobile = Mobile.objects.all()
    return render(request, 'mobile_marketing.html', {
        'all_mobile': all_mobile,  # pass all mobile marketing data to the template,  # pass all social media data to the template
    })

def social_media_marketing(request):
    all_social_media = Social.objects.all()
    return render(request, 'social_media_marketing.html', {
        'all_social_media': all_social_media,  # pass all social media data to the template
    })

def video_marketing(request):
    all_video = Video.objects.all()
    return render(request, 'video_marketing.html', {
        'all_video': all_video,  # pass all video marketing data to the template,  # pass all social media data to the template
    })