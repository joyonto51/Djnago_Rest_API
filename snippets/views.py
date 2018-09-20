import requests
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippet

from django.utils.six import  BytesIO
from snippets.serializers import SnippetSerializer


class SnippetView(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        seri = JSONRenderer().render(serializer.data)
        ser = BytesIO(seri)
        return Response(JSONParser().parse(ser))

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class SnippetDetails(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get(self,request,*args,**kwargs):
        try:
            pk = kwargs['pk']
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return HttpResponse(status=404)

        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(snippet, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)
    #
    # elif request.method == 'DELETE':
    #     snippet.delete()
    #     return HttpResponse(status=204)


# class RestApiResponse(APIView):
#     def get(self, request, *args, **kwargs):
#         data = {'name': 'jayanto', 'bari': 'birol', 'poralekha' : 'nai-apatoto'}
#
#         return Response(data)

class UseAPI(View):
    def get(self, request):
        api = requests.get(url='http://127.0.0.1:8000/snippets/')
        for a in api.json():
            for key,value in sorted(a.items()):
                print(key,' = ', value)
            print('-----------------------------')