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
    author = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=128, blank=False)
    description = MarkdownxField(default="", blank=True, null=True)
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    content = None
    created = models.DateTimeField(editable=False, null=True)
    edited = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.edited = timezone.now()
        if not self.slug:
            self.slug = slugify(self.title + str(timezone.now().timestamp())[-5:])
        super(Post, self).save(*args, **kwargs)


class ArtistImagePost(Post):
    content = models.URLField(blank=False, null=False, default="")

    def __str__(self):
        return "image by %s: %s" % (self.author, self.title)


class ArtistVideoPost(Post):
    content = EmbedVideoField(blank=False, null=False, default="")

    def __str__(self):
        return "video by %s: %s" % (self.author, self.title)


class Article(models.Model):
    title = models.CharField(max_length=64, blank=False)
    text = MarkdownxField(default="")
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)
    image = models.URLField(
        default="http://cdn7.bigcommerce.com/s-viqdwewl26/stencil/8f903ed0-76e7-0135-12e4-525400970412/"
                "icons/icon-no-image.svg")

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.edited = timezone.now()
        if not self.slug:
            self.slug = slugify(self.title + str(timezone.now().timestamp())[-5:])
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return "%s: %s" % (self.id, self.title)


class Artist(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    biography = MarkdownxField(default="")
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    image = models.URLField(
        default="http://cdn7.bigcommerce.com/s-viqdwewl26/stencil/8f903ed0-76e7-0135-12e4-525400970412/"
                "icons/icon-no-image.svg")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Spotlight(models.Model):
    """
    foto met tekst op (titel), link naar article
    """
    left_url = models.URLField(default="/")
    left_image = models.URLField(
        default="http://cdn7.bigcommerce.com/s-viqdwewl26/stencil/8f903ed0-76e7-0135-12e4-525400970412/"
                "icons/icon-no-image.svg")
    left_title = models.CharField(max_length=24, default="", blank=True, null=True)

    right_url = models.URLField(default="/")
    right_image = models.URLField(
        default="http://cdn7.bigcommerce.com/s-viqdwewl26/stencil/8f903ed0-76e7-0135-12e4-525400970412/"
                "icons/icon-no-image.svg")
    right_title = models.CharField(max_length=24, default="", blank=True, null=True)

    created = models.DateTimeField(editable=False, null=True)
    edited = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.edited = timezone.now()
        super(Spotlight, self).save(*args, **kwargs)

    def __str__(self):
        return "Spotlight from %s" % self.created


class Event(models.Model):
    title = models.CharField(max_length=64, default="event")

    def __str__(self):
        return self.title
