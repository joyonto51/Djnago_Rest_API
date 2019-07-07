# Add *LoginView* to this line in  your urls.py file
from django.urls import path

from .views import ListSongsView, LoginView, RegisterUsers

urlpatterns = [
    # ...

    # Some where in your existing urlpatterns list, Add this line
    path('', ListSongsView.as_view(), name="songs"),

    # ...
]
