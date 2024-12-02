from django.urls import path
from .import views


urlpatterns = [
   path('',views.index,name='index'),
   path('pages_blank',views.pages_blank,name='pages_blank'),
    path('pages_contact',views.pages_contact,name='pages_contact'),
    path('pages_error_404',views.pages_error_404,name='pages_error_404'),
    path('pages_faq',views.pages_faq,name='pages_faq'),
    path('pages_login',views.pages_login,name='pages_login'),
   path('pages_register',views.pages_register,name='pages_register'),
   path('pages_general',views.pages_general,name='pages_general'),
   path('pages_profile',views.pages_profile,name='pages_profile'),
   
   path('affiliate_marketing',views.affiliate_marketing,name='affiliate_marketing'),
   path('content_marketing',views.content_marketing,name='content_marketing'),
   path('email_marketing',views.email_marketing,name='email_marketing'),
   path('influencer_marketing',views.influencer_marketing,name='influencer_marketing'),
   path('mobile_marketing',views.mobile_marketing,name='mobile_marketing'),
   path('social_media_marketing',views.social_media_marketing,name='social_media_marketing'),
   path('video_marketing',views.video_marketing,name='video_marketing'),
    
]
 