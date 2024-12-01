# from django.urls import path
# from .import views


# urlpatterns = [
#    path('login_user',views.login_user,name='login'),
#    path('logout_user',views.logout_user,name='logout'),
#    path('register_user',views.register_user,name='register'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountView.as_view(), name='account'),  # default view for users to see their account page
    path('profile', views.Profile_view, name='profile'),
    path('sign-up', views.SignUpView.as_view(), name='sign-up'),
    path('sign-in', views.SignInView.as_view(), name='sign-in'),
    path('sign-out', views.sign_out, name='sign-out'),


]
