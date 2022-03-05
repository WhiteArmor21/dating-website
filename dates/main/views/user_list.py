from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from ..models import UserProfile
from ..serializers.profile import UserProfileSerializer


class UserListView(generics.ListAPIView):
    queryset = UserProfile.objects.order_by('-id')
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)
