from django.urls import include, path
from snippets.views import SnippetViewSet, UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('snippets', SnippetViewSet)
router.register('users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]