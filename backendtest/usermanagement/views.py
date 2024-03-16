from django.core.cache import cache
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView

# Utility function or class method for cache key
def get_cache_key():
    return 'user_registrations_by_month'

# Views
class UserRegistrationByMonthView(APIView):

    @staticmethod
    def get_cache_key():
        return get_cache_key()

    def get(self, request, format=None):
        cache_key = self.get_cache_key()
        cache_time = 2592000  # Time in seconds to keep the cache (30 days)
        # Try to get data from cache
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            registrations = cached_data
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM get_user_registrations_by_month()")
                columns = [col[0] for col in cursor.description]
                registrations = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cache.set(cache_key, registrations, timeout=cache_time)

        return Response(registrations)