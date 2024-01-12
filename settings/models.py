from django.db import models
from django.utils.translation import gettext_lazy as _



class Settings(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='settings')
    subtitle = models.TextField(max_length=500)
    call_us = models.CharField(max_length=25)
    email_us = models.EmailField(max_length=50, verbose_name=_('Email Us'))
    email = models.EmailField(max_length=50)
    phones = models.TextField(max_length=50)
    address = models.TextField(max_length=100)
    android_app = models.URLField(null=True, blank=True, verbose_name=_('Android App URL'))
    ios_app = models.URLField(null=True, blank=True, verbose_name=_('iOS App URL'))
    facebook = models.URLField(null=True, blank=True, verbose_name=_('Facebook URL'))
    youtube = models.URLField(null=True, blank=True, verbose_name=_('YouTube URL'))

    def __str__(self):
        return self.name
