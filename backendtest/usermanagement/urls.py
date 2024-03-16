from django.urls import path
from .views import users_info_view

urlpatterns = [
    path('api/users/monthly-signups', users_info_view.as_view(), name='user-info'),
]

