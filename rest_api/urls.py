from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('snippets.urls')),
    url(r'^email/', include('email_api.urls')),
    url(r'^api_auth/', include('rest_framework.urls')),
]