from django.db import models, IntegrityError
from django.utils.text import slugify
from django.utils.timezone import datetime
from embed_video.fields import EmbedVideoField
from markdownx.models import MarkdownxField


# Create your models here.

class HighScores(models.Model):
    score = models.IntegerField(default=0)
    username = models.CharField(max_length=128, default="None")

    def __str__(self):
        return "%s: %s" % (self.username, self.score)


class Article(models.Model):
    title = models.CharField(max_length=64, blank=False)
    video = EmbedVideoField(blank=True, null=True)
    text = MarkdownxField(default="")
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + str(datetime.now().timestamp())[-5:])
        super(Article, self).save(*args, **kwargs)
