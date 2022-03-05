import os
from django.core.management.base import BaseCommand, CommandError
from dates.settings import FIXTURE_PATH, API_URL
import json
from main.models import UserProfile
from usermedia.models import UserMedia
import requests
from rest_framework.authtoken.models import Token


def get_user_token(username):
    user = UserProfile.objects.get(username=username)
    token = Token.objects.get_or_create(user=user)
    return token

class Command(BaseCommand):
    def handle(self, *args, **options):
        user_file = os.path.join(FIXTURE_PATH, 'users.json')
        with open(user_file,'r') as f:
            jdata = json.loads(f.read())
            UserMedia.objects.all().delete()
            for user in jdata['users']:
                token = get_user_token(user['username'])
                print(user['username'])
                print(token[0].key)
                for image in user['images']:
                    filepath = os.path.join(FIXTURE_PATH, 'images', 'image.jpg')
                    files = {'image' : open(filepath, 'rb')}
                    rez = requests.post(
                        API_URL+'usermedia/add_image',
                        headers={'Authorization': 'Token %s' % token[0].key},
                        files=files,
                        data=image)
                    print(rez)
                    if rez.status_code == 200:
                        print(json.loads(rez.text))
                    else:
                        print('error')
                        print(rez.text)


