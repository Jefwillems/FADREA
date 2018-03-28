from django.db import models


# Create your models here.

class HighScores(models.Model):
    score = models.IntegerField(default=0)
    username = models.CharField(max_length=128, default="None")

    def __str__(self):
        return "%s: %s" % (self.username, self.score)
