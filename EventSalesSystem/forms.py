from django import forms
from django.forms import ModelForm
from .models import Social

class EventForm(ModelForm):
    class Meta:
        model = Social
        fields = ('image','product','price','quantity_sold','revenue')