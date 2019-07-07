from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token

from music.views import RegisterUsers, LoginView

schema_view = get_schema_view(title='Pastebin API',)

# Add *LoginView* to this line in  your urls.py file

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-token-auth/', obtain_jwt_token, name='create-token'),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth-register/', RegisterUsers.as_view(), name="auth_register"),

    re_path('api/(?P<version>(v1|v2))/', include('music.urls')),
    path('', include('snippets.urls')),


    path('email/', include('email_api.urls')),
    path('attendance/', include('attendance.urls')),
    path('attendance/', include('attendance.urls')),
    path('api_auth/', include('rest_framework.urls')),
    path('schema/', schema_view),
]

