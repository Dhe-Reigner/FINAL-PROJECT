from django.db import models

DATE = [
]


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)    
    image = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
     
    def __str__(self):
        return self.name
     
class EventDetail(models.Model):
    image = models.ImageField(Event,upload_to='images/', default='', blank=True, null=True)
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    key_details = models.TextField()
    # attendees = models.ManyToManyField('EventAttendee')
    # speaker = models.ForeignKey('EventSpeaker', on_delete=models.CASCADE)
    date = models.DateTimeField()                        
    location = models.CharField(Event, max_length=100)
    phone_number = models.CharField(max_length=20)
    website = models.URLField()
    description = models.TextField(Event)
    
    def __str__(self):
        return str(self.event_name)
    
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip_code', max_length=20)
    phone = models.CharField('Contact Phone', max_length=20, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name