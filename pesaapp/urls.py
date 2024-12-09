from django.urls import path
from pesaapp.views import form, StkCallbackView, PaymentView, DefaultHomeView,ViewMpesaPayments, ViewMpesaRequests,payvia_webapp

urlpatterns = [
    path('stk-callback/', StkCallbackView.as_view()),
    path('pay', PaymentView.as_view()),
    path('payments', ViewMpesaPayments.as_view()),
    path('requests', ViewMpesaRequests.as_view()),
    path('webapp', payvia_webapp),
    path('home', DefaultHomeView.as_view()),
    # path('', payvia_webapp),
     path('pay/', payvia_webapp, name='payvia_webapp'),
]

