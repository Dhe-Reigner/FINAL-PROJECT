from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name','location','image','description','start_date','end_date')
        
      
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Location'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Event Description'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
        }