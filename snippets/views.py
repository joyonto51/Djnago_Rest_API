import requests, sendgrid

from sendgrid.helpers.mail import *

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.six import  BytesIO
from django.views.generic.base import View

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, mixins
from rest_framework.views import APIView

from snippets.models import Snippet

from snippets.serializers import SnippetSerializer


class SnippetView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer




# class RestApiResponse(APIView):
#     def get(self, request, *args, **kwargs):
#         data = {'name': 'jayanto', 'bari': 'birol', 'poralekha' : 'nai-apatoto'}
#
#         return Response(data)

class UseAPI(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'data_send.html')

    def post(self, request, *args, **kwargs):

        title = request.POST['title']
        code = request.POST['code']
        linenos = request.POST['linenos']
        language = request.POST['language']
        style = request.POST['style']

        data = {"title":title, "code":code, "linenos":linenos, "language":language, "style":style}
        print(data)
        api = requests.post(url='http://127.0.0.1:8000/snippets/', data=data)

        return HttpResponseRedirect(reverse('snippet_list'))

class EmailSendView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'email.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('text')

        sg = sendgrid.SendGridAPIClient(apikey='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')
        from_email = Email("aarosh.itsd@gmail.com")
        to_email = Email(email)

        content = Content("text/plain", text)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())

        print(response.status_code)
        print(response.body)
        print(response.headers)

        return HttpResponseRedirect(reverse('email'))