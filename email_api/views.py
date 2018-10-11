import requests
import sendgrid
from django.views import View
from rest_framework.response import Response
from sendgrid.helpers.mail import *

from rest_framework.views import APIView

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .serializers import EmailSerializers



class EmailSendAPI(APIView):
    def get(self,request,*args,**kwargs):
        serializers = EmailSerializers()
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializers = EmailSerializers(data=request.data)

        if serializers.is_valid():
            print(serializers.data)
            email = serializers.data['to_email']
            subject = serializers.data['email_subject']
            body = serializers.data['email_body']
            print(email,subject,body)

            sg = sendgrid.SendGridAPIClient(apikey='SG.OIISEHmmQxOahwt0XLZ_AA.Y - iqm_wajdHnJu6P2uGEphJNfM0nTUNBbxfvn3HaBsY')
            from_email = Email("aarosh.itsd@gmail.com")
            to_email = Email(email)

            content = Content("text/plain", body)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())

            serializers.from_email = from_email
            serializers.save()
            print('Email has been sent')

            print(response.status_code)
            print(response.body)
            print(response.headers)

        return Response("it's okay")



class EmailSendView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'email.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('text')

        data = {"to_email":email, "email_subject":subject, "email_body": body}

        api = requests.post(url='http://127.0.0.1:8000/email/api/', data=data)
        print(api)

        return HttpResponseRedirect(reverse('email_send'))
