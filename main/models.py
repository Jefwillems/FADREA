from django.db import models

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
    video = EmbedVideoField()
    text = MarkdownxField(default="")
