from django.db import models, IntegrityError
from django.utils.text import slugify
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from polymorphic.models import PolymorphicModel
from markdownx.models import MarkdownxField


# Create your models here.

class HighScores(models.Model):
    score = models.IntegerField(default=0)
    username = models.CharField(max_length=128, default="None")

    def __str__(self):
        return "%s: %s" % (self.username, self.score)


class Post(PolymorphicModel):
    author = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='imageposts')
    title = models.CharField(max_length=128, blank=False)
    description = MarkdownxField(default="", blank=True, null=True)
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    content = None
    created = models.DateTimeField(editable=False)
    edited = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.edited = timezone.now()
        if not self.slug:
            self.slug = slugify(self.title + str(timezone.now().timestamp())[-5:])
        super(Post, self).save(*args, **kwargs)


class ArtistImagePost(Post):
    content = models.URLField(blank=False, null=False, default="")


class ArtistVideoPost(Post):
    content = EmbedVideoField(blank=False, null=False, default="")


class Article(models.Model):
    title = models.CharField(max_length=64, blank=False)
    text = MarkdownxField(default="")
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + str(timezone.now().timestamp())[-5:])
        super(Article, self).save(*args, **kwargs)


class Artist(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    biography = MarkdownxField(default="")
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)


class Spotlight(models.Model):
    """
    foto met tekst op (titel), link naar article
    """
    pass
