from django.conf.urls import url
from django.urls import path
from .views import SendGridApi


urlpatterns = [
    path('api_get/', SendGridApi.as_view(), name= 'sendgrid_api'),
]