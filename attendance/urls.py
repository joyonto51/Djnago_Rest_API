from django.urls import path
from attendance.views import TakeAttendanceView, SelectClassSectionView

urlpatterns = [
    path('take-attendance/', TakeAttendanceView.as_view(), name='take_attendance'),
    path('class-list/', SelectClassSectionView.as_view(), name='select_class'),
]