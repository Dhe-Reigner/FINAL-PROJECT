from django import forms
from django.forms import ModelForm
# from .models import Social
from.models import User_Profile
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study']
        labels = {
            'student_number': 'Student Number',
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'field_of_study' : 'Field of Study',
            
        }
        widgets = {
        'student_number': forms.NumberInput(attrs={'class':'form-control'}),
        'first_name': forms.TextInput(attrs={'class':'form-control'}),
        'last_name' :forms.TextInput(attrs={'class':'form-control'}),
        'email' :forms.EmailInput(attrs={'class':'form-control'}),
        'field_of_study' :forms.TextInput(attrs={'class':'form-control'}),
        
            
    }    

# class EventForm(ModelForm):
#     class Meta:
#         model = Social
#         fields = ('image','product','price','quantity_sold','revenue')
        
        
class User_ProfileForm(ModelForm):
    class Meta:
        model = User_Profile
        fields = ['full_name','about','company','job','country','address','phone','email']
        labels = {
            'full_name': 'Full Name',
            'about': 'About',
            'company': 'Company',
            'job': 'Job',
            'country': 'Country',
            'address': 'Address',
            'phone': 'Phone',
            'email': 'Email',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company'}),
            'job': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
        


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study']
        labels = {
            'student_number': 'Student Number',
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'field_of_study' : 'Field of Study',
            
        }
        widgets = {
        'student_number': forms.NumberInput(attrs={'class':'form-control'}),
        'first_name': forms.TextInput(attrs={'class':'form-control'}),
        'last_name' :forms.TextInput(attrs={'class':'form-control'}),
        'email' :forms.EmailInput(attrs={'class':'form-control'}),
        'field_of_study' :forms.TextInput(attrs={'class':'form-control'}),
        
            
    }    