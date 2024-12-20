from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='my_index'),
     path('stk',views.stk,name='my_stk'),
    path('display/',views.display,name='my_display'),
    # path('about/',views.about,name='my_about'),
    # path('contact/',views.contact,name='my_contact'),
    # path('event/<int:event_id>/',views.event_detail,name='my_event_detail'),
    # path('event/create/',views.event_create,name='my_event_create'),
    path('event_detail/<int:event_id>/',views.event_detail,name='event_detail'),
    path('add_event/',views.add_event,name='add_event'),
    path('list_venues/',views.list_venues,name='list_venues'),
    path('show_venue/<venue_id>/',views.show_venue,name='show_venue'),
    path('daraja/stk_push', views.stk_push_callback,name='stk_push_callback'),
    
    path('kids', views.kids,name='my_kids'),
   path('lifestyle', views.lifestyle,name='my_lifestyle'),
   path('movies', views.movies,name='my_movies'),
    

   
]





# from django.urls import path 
# from . import views

# urlpatterns = [
# path('route', views.route,name='route'),
# path('map', views.map, name='map')
# ]