from django.urls import path
from .views import  EmailSendView, EmailSendAPI

urlpatterns = [
    path('send/', EmailSendView.as_view(), name='email_send'),
    path('api/', EmailSendAPI.as_view(), name='email_api')
]
