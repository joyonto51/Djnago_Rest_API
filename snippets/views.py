from rest_framework.decorators import renderer_classes, action
from rest_framework.reverse import reverse
from rest_framework import generics, mixins, response, renderers
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly

from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.hightlighted)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('snippet-list', request=request, format=format),
            'snippets': reverse('user-list',request=request, format=format)
        })
