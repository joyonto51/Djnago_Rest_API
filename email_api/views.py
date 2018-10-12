import requests

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from email_api.models import Email
from rest_api.settings import EMAIL_HOST_USER
from .serializers import EmailSerializers


class EmailAPIView(APIView):
    def get(self,request,*args,**kwargs):
        serializers = EmailSerializers()
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializers = EmailSerializers(data=request.data)
        username = request.data['username']
        password = request.data['password']

        user = User.objects.get(id=2)

        if (username==user.username and password==user.password) and serializers.is_valid():
            email_object = serializers.save()
            email = Email.objects.get(id=email_object.id)
            email.from_email = EMAIL_HOST_USER
            email.save()

            email = serializers.data['to_email']
            subject = serializers.data['email_subject']
            body = serializers.data['email_body']

            self.send_api_mail(subject,body,[email,])

            return Response(status=status.HTTP_202_ACCEPTED)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def send_api_mail(self, subject='', message='', recipients=''):
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

        user = User.objects.get(username='joyonto')

        data = {"username":user.username, "password":user.password, "to_email":email, "email_subject":subject, "email_body":body}

        api = requests.post(url='http://127.0.0.1:8000/email/api/', data=data)

        return HttpResponseRedirect(reverse('email_send'))
