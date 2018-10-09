from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetList, SnippetDetails, UserList, UserDetail, ApiRoot, SnippetHightlight

urlpatterns = [
    url(r'^$', ApiRoot.as_view()),

    url(r'^snippets/$', SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetails.as_view(), name='snippet-detail'),

    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),

    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', SnippetHightlight.as_view(), name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)