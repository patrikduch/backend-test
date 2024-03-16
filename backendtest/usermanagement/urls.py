from django.urls import path
from .views import users_info_view
from .views import AdminUserCreate

urlpatterns = [
    path('api/users/monthly-signups', users_info_view.as_view(), name='user-info'),
    path('api/admin/create/', AdminUserCreate.as_view(), name='admin-create'),
]

