from django.db import models
from django.conf import settings
from django.contrib.auth import base_user as User
from django.core.validators import RegexValidator


# Create your models here.
class Audio(models.Model):
    name = models.CharField(max_length=255)
    transcription = models.TextField(blank=True, null=True)
    details = models.CharField(max_length=255, blank=True)
    tags = models.TextField(blank=True)
    annotator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    transcribed = models.BooleanField(default=False)
    url = models.CharField(max_length=255)


    def isTanscribed(self):
        return self.transcribed

    def __str__(self):
        return self.name


class Charset(models.Model):
    data = models.TextField(default="()'aA-àÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ "
                            , null=True)

    def __str__(self):
        return "Charset"
