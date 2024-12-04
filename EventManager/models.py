from django.db import models
from datetime import datetime
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

DATE = [
]


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    # address = models.CharField(max_length=200)
    # latitude = models.FloatField()
    # longitude = models.FloatField()
    
    
    def __str__(self):
        return self.name
class Display(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateField(default="2024-01-01")
    name = models.CharField(default='', max_length=100)
    
    def __str__(self):
        return str(self.name)

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, max_length=100)     
    image = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/',blank=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=datetime(2024, 1, 1))
    end_date = models.DateTimeField(default=datetime(2024, 1, 1))
    event_detail = models.TextField(default='', blank=True, null=True)
    
     
    def __str__(self):
        return self.name
    
class EventDetail(models.Model):
    image = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/',blank=True)
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    key_details = models.TextField()
    # attendees = models.ManyToManyField('EventAttendee')
    # speaker = models.ForeignKey('EventSpeaker', on_delete=models.CASCADE)
    date = models.DateTimeField()                        
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    website = models.URLField()
    description = models.TextField()
    
    
    def __str__(self):
        return str(self.event_name)
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.event_name)
        canvas = Image.new('RGB',(290,290),'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img, (0, 0))
        fname = f'qr_code-{self.event_name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, format='PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
        
    
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip_code', max_length=20)
    phone = models.CharField('Contact Phone', max_length=20, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name