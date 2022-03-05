from rest_framework import serializers
from usermedia.models import UserMedia

class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMedia
        fields = [
            'id',
            'image',
            'title',
            'is_main'
        ]