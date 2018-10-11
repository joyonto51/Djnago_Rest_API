from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API',)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('snippets.urls')),
    url(r'^email/', include('email_api.urls')),
    url(r'^sendgrid/', include('sengrid_api.urls')),
    url(r'^api_auth/', include('rest_framework.urls')),
    url(r'^schema/', schema_view),
]

