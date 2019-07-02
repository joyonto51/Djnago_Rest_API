from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API',)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    path('email/', include('email_api.urls')),
    path('attendance/', include('attendance.urls')),
    path('api_auth/', include('rest_framework.urls')),
    path('schema/', schema_view),
]

