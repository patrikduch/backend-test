from django.core.cache import cache
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView

class users_info_view(APIView):

    def get(self, request, format=None):
        # Create a unique cache key based on the endpoint name or path
        cache_key = 'user_registrations_by_month'
        # Try to get cached data
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            # If cached data is available, use it
            registrations = cached_data
        else:
            # If no cached data, fetch the data from the database
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM get_user_registrations_by_month()")
                columns = [col[0] for col in cursor.description]
                registrations = [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
            # Cache the data for next time, set the cache to expire after some time e.g., 1 hour
            cache.set(cache_key, registrations, timeout=3600)

        return Response(registrations)