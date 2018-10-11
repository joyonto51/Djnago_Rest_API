from django.urls import path
from .views import  EmailSendView, EmailSendAPIView

urlpatterns = [
    path('api/', EmailSendAPIView.as_view(), name="email_api"),
    path('send/', EmailSendView.as_view(), name="email_send"),
]
