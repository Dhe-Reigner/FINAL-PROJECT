from django.shortcuts import render,redirect
from django.contrib.auth  import authenticate, login, logout 
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib .auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('my_index')
        else:
            messages.success(request, 'Invalid credentials!!! Please Try Again')
            return redirect('login')
    else:
      return render(request, 'authenticate/login.html',{})
def logout_user(request):
    logout(request)
    messages.success(request, 'You are Logged Out')
    return redirect('my_display')

def register_user(request):
    messages.success(request, 'You are Logged Out')
    return redirect('my_display')

# def register_user(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registration Successful!!!')
#             return redirect('login')
#         else:
#             messages.error(request, 'Registration Failed!!!')
#             return redirect('register')
#     else:
#         form = UserCreationForm()
#         return render(request, 'authenticate/register.html', {'form': form})

def register_user(request):
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            messages.success(request, 'Registration Successful!!!')
            return redirect('my_index')
        else:
            form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()  # An unbound form
    return render(request,'authenticate/register.html',{'form':form})




# from django.shortcuts import render, redirect, reverse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth import login, logout, authenticate
# from django.conf import settings
# from django.http import JsonResponse
# from django.views.generic.edit import FormView
# from django.views.generic.base import TemplateView
# from django.utils.decorators import method_decorator

# from FinalProject.mixins import(
#     AjaxFormMixin,
#     reCAPTCHAValidation,
#     FormError,
#     RedirectParams
# )

# from .forms import(
#     UserForm,
#     UserProfileForm,
#     AuthForm,
# )
# result = "error"
# message = "There was an error updating your profile, please try again"
    
# class AccountView(TemplateView):
#     '''Generic FormView with our mixin to display user account page'''
#     template_name = 'users/account.html'
    
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
    
# def Profile_view(request):
#     '''function view to allow members update their profile'''
#     user = request.user
#     up = user.userprofile
#     form = UserProfileForm(instance = up)
    
   
#     if request.is_ajax():
#         # if request.method == 'POST':
#             form = UserProfileForm(data = request.POST, instance = up)
#             if form.is_valid():
#                 obj = form.save()
#                 obj.has_profile = True
#                 obj.save()
#                 result = "success"
#                 message = "Your Profile has been Updated Successfully"
#             else:
#                 message = FormError(form)
#             data = {'result': result, 'message': message}
#             return JsonResponse(data)
        
#     else:
#         context = {'form': form}
#         context['google_api_key'] = settings.GOOGLE_API_KEY
#         context['base_country'] = settings.BASE_COUNTRY
        
#         return render(request, 'users/profile.html', context)
    


# class SignUpView(AjaxFormMixin, FormView):
#     '''Generic FormView with our mixin to handle user sign up with reCAPTURE security key'''
#     template_name = 'users/signup.html'
#     form_class = UserForm
#     success_url = "/"
    
#     result = "Error"
#     message = "There was an error registering your account, please try again"
    
#     #reCAPTURE key required in context
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['recaptcha_site_key'] = settings.RECAPTCHA_PUBLIC_KEY
#         return context
    
#     #overwrite the mixin logic to get, check and save reCAPTCHA score
#     def form_valid(self, form):
#         response = super(AjaxFormMixin, self).form_valid(form)
#         if self.request.is_ajax():
#             token  =form.cleaned_data.get('token')
#             captcha = reCAPTCHAValidation(token)
#             if captcha['success']:
#                 obj  =form.save()
#                 obj.email = obj.username
#                 obj.save()
#                 up  =obj.userprofile
#                 up.captcha_score = float(captcha['score'])
#                 up.save()
                
#                 login(self.request, obj, backend =  'django.contrib.auth.backends.ModelBackend')
                
#                 #change result & message on success
#                 result = "success"
#                 message = "Your account has been created successfully"
                
#             data = {'result': result, 'message': message}
#             return JsonResponse(data)
        
#         return response
    
# class SignInView(AjaxFormMixin, FormView):
#     '''Generic FormView with our mixin to handle user sign in'''
#     template_name = 'users/signin.html'
#     form_class = AuthForm
#     success_url = "/"
    
#     def form_valid(self, form):
#         response = super(AjaxFormMixin, self).form_valid(form)
#         if self.request.is_ajax():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
            
#             #attempt to  authenticate user
#             user = authenticate(self.request, username = username, password = password)
            
#             if user is not None:
#                 login(self.request, user, backend =  'django.contrib.auth.backends.ModelBackend')
                
#                 #change result & message on success
#                 result = "success"
#                 message = "You have successfully logged in"
                
#             else:
#                 result = "error"
#                 message = "Invalid credentials for log in, please try again"
                
#             data = {'result': result, 'message': message}
#             return JsonResponse(data)
        
#         return response
    
    
# def sign_out(request):
#     '''function view to handle user sign out'''
#     logout(request)
#     return redirect(reverse('users:sign-in'))
