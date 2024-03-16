from django.shortcuts import render

# Create your views here.
class UsersInfoView(APIView):

    def get(self, request, format=None):
        users = User.objects.all()  # Gets all user objects
        serializer = UsersSerializer(users, many=True)  # Serialize the list of users
        return Response(serializer.data)