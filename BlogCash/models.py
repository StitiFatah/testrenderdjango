from django.db import models


class TestImages(models.Model):

    name = models.CharField(max_length=200)
    image = models.FileField()
