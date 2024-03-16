from django.urls import path
from .views import UserRegistrationByMonthView

urlpatterns = [
    path('api/users/monthly-signups', UserRegistrationByMonthView.as_view(), name='user-info'),
]

