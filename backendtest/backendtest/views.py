from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsersSerializer

class UsersInfoView(APIView):

    def get(self, request, format=None):
        users = User.objects.all()  # Gets all user objects
        serializer = UsersSerializer(users, many=True)  # Serialize the list of users
        return Response(serializer.data)