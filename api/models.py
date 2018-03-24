from django.contrib.auth.models import AbstractUser
from django.db import models


# TODO from django.core.files.storage import FileSystemStorage
# TODO fs = FileSystemStorage(location='/media/photos')


class Profile(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=128, blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False)
