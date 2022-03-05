from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from ..serializers.user_request import UserRequestSerializer
from main.models import UserMatch
from rest_framework.authtoken.models import Token
from main.models import UserProfile
import json


class RegistrationView(APIView):
    '''
    User registration.
    -----------------
    '''

    permission_classes = (
        AllowAny,
    )

    request_body = UserRequestSerializer

    def post(self, request, format=None):
        obj = UserRequestSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response({'message': 'Ok'})

class UserMatchView(APIView):

    permission_classes = (
        IsAuthenticated,
    )

    def post(self, request):
        user = Token.objects.get(key=request.data.get("auth")).user
        liked_person = UserProfile.objects.get(username=request.data.get("user"))

        if user == liked_person:
            return Response({'message': "User can't like himself"})
        elif UserMatch.objects.filter(user=user).filter(liked_person=liked_person):
            return Response({'message': "This match already exsists"})
        elif UserMatch.objects.filter(user=liked_person).filter(liked_person=user):
            resp = Response({'message': "Reciprocity!"})
        obj = UserMatch(user=user, liked_person=liked_person)
        obj.save()
        return resp



