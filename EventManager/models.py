from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)    
    image = models.ImageField(default='m1.jpg', blank=True)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self):
        return self.name
                        
