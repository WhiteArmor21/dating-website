from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class UserMatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_person')

    def __str__(self):
        return "User {} likes User {}".format(self.user, self.liked_person)


image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/users_photo/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}users_photo/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/users_photo/<filename>
    return u'{0}'.format(filename)


class UserProfile(User):
    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS)
    image = models.ImageField(blank=True, upload_to=image_directory_path, storage=image_storage)
