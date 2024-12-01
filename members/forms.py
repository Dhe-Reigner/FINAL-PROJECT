from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Your First Name..'}))
    last_name = forms.CharField(max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Your Last Name..'}))
    email = forms.EmailField(max_length=300, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Your First Name..'}))
    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': '*Password..','class': 'password'}))
    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': '*Confirm Password..','class': 'password'}))
    
    #reCAPTCHA token
    token = forms.CharField(
        widget = forms.HiddenInput())
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
class AuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=254, required=True,
         widget=forms.TextInput(attrs={'placeholder': '*Username..'}))
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': '*Password..','class': 'password'}))
    
    class Meta:
        model = User
        fields = ('username', 'password')
    
    
class UserProfileForm(forms.ModelForm):
    address = forms.CharField(max_length=100, required=True,
        widget=forms.HiddenInput())
    city = forms.CharField(max_length=50, required=True,
        widget=forms.HiddenInput())
    state = forms.CharField(max_length=50, required=True,
        widget=forms.HiddenInput())
    zip_code = forms.CharField(max_length=10, required=True,
        widget=forms.HiddenInput())
    country = forms.CharField(max_length=50, required=True,
        widget=forms.HiddenInput())
    phone_number = forms.CharField(max_length=20, required=True,
        widget=forms.HiddenInput())
    website = forms.URLField(max_length=200, required=False,
        widget=forms.HiddenInput())
    longitude = forms.CharField(max_length=50, required=False,
        widget=forms.HiddenInput())
    latitude = forms.CharField(max_length=50, required=False,
        widget=forms.HiddenInput())
    
    class Meta:
        model = UserProfile
        fields = ('address', 'city', 'state', 'zip_code', 'country', 'phone_number', 'website', 'longitude', 'latitude')