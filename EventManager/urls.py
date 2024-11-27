from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='my_index'),
    # path('about/',views.about,name='my_about'),
    # path('contact/',views.contact,name='my_contact'),
    # path('event/<int:event_id>/',views.event_detail,name='my_event_detail'),
    # path('event/create/',views.event_create,name='my_event_create'),
    path('event_detail/',views.event_detail,name='event_detail'),
    path('add_event/',views.add_event,name='add_event'),
]
