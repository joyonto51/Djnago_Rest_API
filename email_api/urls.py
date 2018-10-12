from django.urls import path
from .views import  EmailSendView, EmailAPIView

urlpatterns = [
    path('api/', EmailAPIView.as_view(), name="email_api"),
    path('send/', EmailSendView.as_view(), name="email_send"),
]
