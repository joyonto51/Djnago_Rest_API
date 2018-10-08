from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetView, SnippetDetails, UseAPI

urlpatterns = [
    url(r'^snippets/$', SnippetView.as_view(), name='snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetails.as_view()),
    url(r'^data/', UseAPI.as_view(), name='data'),

]

urlpatterns = format_suffix_patterns(urlpatterns)