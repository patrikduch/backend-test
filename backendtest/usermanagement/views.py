from django.core.cache import cache
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import AdminUserSerializer

# Utility function or class method for cache key
def get_cache_key():
    return 'user_registrations_by_month'

# Views
class users_info_view(APIView):

    @staticmethod
    def get_cache_key():
        return get_cache_key()

    def get(self, request, format=None):
        cache_key = self.get_cache_key()
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            registrations = cached_data
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM get_user_registrations_by_month()")
                columns = [col[0] for col in cursor.description]
                registrations = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cache.set(cache_key, registrations, timeout=3600)

        return Response(registrations)
    

class AdminUserCreate(APIView):

    @staticmethod
    def get_cache_key():
        return get_cache_key()

    def post(self, request, format=None):
        serializer = AdminUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            cache_key = self.get_cache_key()
            if cache.get(cache_key) is not None:
                cache.delete(cache_key)

            return Response({"id": user.id, "username": user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)