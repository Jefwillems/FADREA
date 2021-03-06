from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField


class Profile(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=128, blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False)

    def full_name(self):
        name = '%s %s' % (self.first_name, self.last_name)
        return name.strip()


class Members(models.Model):
    first_name = models.CharField(max_length=64, default="")
    last_name = models.CharField(max_length=64, default="")
    email = models.EmailField(max_length=128, default="info@fadrea.be")
    functie = models.CharField(max_length=128, default="")
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='members', null=True)

    def full_name(self):
        name = '%s %s' % (self.first_name, self.last_name)
        return name.strip()

    def __str__(self):
        return self.full_name()


class Contact(models.Model):
    biography = MarkdownxField()
    created = models.DateField(blank=True, null=True)

    def __str__(self):
        return 'Contact info'

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        return super(Contact, self).save(*args, **kwargs)
