from django.contrib import admin
from .models import Event
from .models import EventDetail
from .models import Venue
from .models import Display

# Register your models here.
admin.site.register(Event)
admin.site.register(EventDetail)
admin.site.register(Venue)
admin.site.register(Display)