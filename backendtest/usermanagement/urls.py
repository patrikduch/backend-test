from django.urls import path
from .views import UserRegistrationByMonthView
from .views import AdminUserCreate

urlpatterns = [
    path('api/users/monthly-signups', UserRegistrationByMonthView.as_view(), name='user-info'),
    path('api/admin/create/', AdminUserCreate.as_view(), name='admin-create'),
]

