import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class SendGridApi(APIView):
    def get(self,request,*args,**kwargs):
        API_KEY = "SG.OIISEHmmQxOahwt0XLZ_AA.Y - iqm_wajdHnJu6P2uGEphJNfM0nTUNBbxfvn3HaBsY"
        email = requests.get("https://api.sendgrid.com/v3/templates/ Accept: -H Authorization: Bearer {} -H Content-Type: application/json".format(API_KEY))
        print(email)
        return Response(email)