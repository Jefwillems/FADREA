from django.db import models


class HighScores(models.Model):
    score = models.IntegerField(default=0)
    username = models.CharField(max_length=128, default="None")
