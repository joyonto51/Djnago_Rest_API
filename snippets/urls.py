from django.conf.urls import url
from snippets import views
from snippets.views import SnippetView, SnippetDetails, UseAPI

urlpatterns = [
    url(r'^snippets/$', SnippetView.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetails.as_view()),
    url(r'^data/', UseAPI.as_view(), name='data'),
]