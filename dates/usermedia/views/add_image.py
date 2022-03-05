from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser
from usermedia.serializers.image import UserImageSerializer
from usermedia.models import UserMedia


class AddImageView(generics.CreateAPIView):
    queryset = UserMedia.objects.all()
    serializer_class = UserImageSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    parser_classes = (MultiPartParser, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.userprofile)
