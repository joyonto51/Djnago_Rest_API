from django.conf.urls import url
from .views import  EmailSendView

urlpatterns = [
    url(r'^', EmailSendView.as_view(), name='email'),
]
