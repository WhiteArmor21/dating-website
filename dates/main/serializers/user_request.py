from rest_framework import serializers
from main.models import UserProfile


class UserRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    gender = serializers.ChoiceField(choices=['F', 'M', 'O'])

    def validate_username(self, value):
        error = False
        try:
            UserProfile.objects.get(username=value)
            error = True
        except:
            pass

        if error:
            raise serializers.ValidationError('This username is already exists')

        return value

    def save(self, **kwargs):
        profile = UserProfile()
        profile.username = self.validated_data['username']
        profile.set_password(self.validated_data['password'])
        profile.gender = self.validated_data['gender']
        profile.save()
        return profile