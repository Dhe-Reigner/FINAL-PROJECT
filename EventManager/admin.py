from django.contrib import admin
from .models import Event
from .models import EventDetail
from .models import Venue
from .models import Display
from .models import Location
from .models import Kid
from .models import Lifestyle
from .models import Movie

# Register your models here.
admin.site.register(Event)
admin.site.register(EventDetail)
admin.site.register(Venue)
admin.site.register(Display)
admin.site.register(Location)
admin.site.register(Kid)
admin.site.register(Lifestyle)
admin.site.register(Movie)