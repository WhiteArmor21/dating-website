from rest_framework import serializers
from ..models import UserProfile
from dates.settings import BACKEND_URL
from usermedia.models import UserMedia


class UserProfileSerializer(serializers.ModelSerializer):
    main_photo = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            'id',
            'username',
            'gender',
            'main_photo',
        ]

    def get_main_photo(self, obj):
        try:
            media = UserMedia.objects.get(user=obj, is_main=True, type_media='photo')
            return BACKEND_URL+media.image.url
        except Exception as ex:
            return 'no image'