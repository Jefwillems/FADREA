from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=128, blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False)

    def full_name(self):
        name = '%s %s' % (self.first_name, self.last_name)
        return name.strip()
