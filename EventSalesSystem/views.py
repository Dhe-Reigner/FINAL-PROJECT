from django.shortcuts import render
from.models import Dashboard
from .models import Social
from.models import Content
from.models import Email
from.models import Influencer
from.models import Affiliate
from.models import Video
from.models import Mobile
from.models import RemoteWork 
from.models import course
from.models import User_Profile
from.models import Student
from .forms import StudentForm

# Create your views here.
# def index(request):
#     return render(request, 'pages/index.html', {})

def index(request):
    all_dashboard = Dashboard.objects.all()
    return render(request, 'pages/index.html', {
        'all_dashboard': all_dashboard,  # pass all dashboard data to the template,  # pass all social media data to the template
    })

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

def dashboard(request):
    all_dashboard = Dashboard.objects.all()
    return render(request, 'dashboard.html', {
        'all_dashboard': all_dashboard,  # pass all dashboard data to the template,  # pass all social media data to the template
    })
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
    return render(request, 'influencer_marketing.html', {
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
    
def remote_works(request):
    all_remote_work = RemoteWork.objects.all()
    return render(request, 'remote_works.html', {
        'all_remote_work': all_remote_work,  # pass all remote work data to the template,  # pass all social media data to the template
    })
    
    

def courses(request):
    all_courses = course.objects.all()
    return render(request, 'courses.html', {
        'all_courses': all_courses,  # pass all courses data to the template,  # pass all social media data to the template
    })
    
def user_profile(request):
    all_user_profile = User_Profile.objects.all()
    return render(request, 'user_profile.html', {
        'all_user_profile': all_user_profile,  # pass all user_profile data to the template,  # pass all social media data to the template
    })
    
def list_students(request):
    return render(request, 'students/list_students.html',{
        'students':Student.objects.all()
    })
def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse("list_students"))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_mean_score = form.cleaned_data['mean_score']
            
            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                mean_score = new_mean_score
            )
            new_student.save()
            return render(request, 'students/add.html',{
                'form':StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
        return render(request, 'students/add.html',{
            'form': StudentForm()
        })        
 
def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html',{
                'form': form,
                'success': True
            }) 
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html',{
        'form': form
    })
        
def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('list_students'))        
        
    