from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetList, SnippetDetails, UserList, UserDetail

urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view(), name='snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetails.as_view()),
    url(r'^users/$', UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)