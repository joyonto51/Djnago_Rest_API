import requests

from django.core.mail import send_mail
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from email_api.models import Email
from rest_api.settings import EMAIL_HOST_USER
from .serializers import EmailSerializers


class EmailSendAPIView(APIView):
    def get(self,request,*args,**kwargs):
        serializers = EmailSerializers()
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializers = EmailSerializers(data=request.data)

        if serializers.is_valid():
            email_object = serializers.save()
            email = Email.objects.get(id=email_object.id)
            email.from_email = EMAIL_HOST_USER
            email.save()

            email = serializers.data['to_email']
            subject = serializers.data['email_subject']
            body = serializers.data['email_body']

            self.send_email(subject,body,recipients=[email,])

        return Response("Email has been sent")

    def send_email(self, subject='', message='', recipients=''):
        mail = send_mail(subject, message, EMAIL_HOST_USER, recipients, fail_silently=True)

        if mail == 0:
            print('Sending mail failed.')
            print(message)

        return



class EmailSendView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'email.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('text')

        data = {"to_email":email, "email_subject":subject, "email_body": body}

        api = requests.post(url='http://127.0.0.1:8000/email/api/', data=data)

        return HttpResponseRedirect(reverse('email_send'))
