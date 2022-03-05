from django.core.management.base import BaseCommand, CommandError
from dates.settings import FIXTURE_FILE, API_URL
import json
import requests
from main.models import UserProfile


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(FIXTURE_FILE, 'r') as f:
            jdata = json.loads(f.read())

        UserProfile.objects.all().delete()

        for user in jdata['administrators']:
            profile = UserProfile()
            profile.username = user['username']
            profile.set_password(user['password'])
            profile.is_staff = True
            profile.is_superuser = True
            profile.save()
            print('Created %s' % profile.username)

        for user in jdata['users']:
            rez = requests.post(API_URL+'account/registration', json=user)
            print('Created %s' % user['username'])
            print(json.loads(rez.content)['message'])

