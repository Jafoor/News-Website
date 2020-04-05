from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length = 30)
    about = models.TextField()
    abouttxt = models.TextField(default = "")
    fb = models.CharField(default = "-",max_length = 30)
    tw = models.CharField(default = "-",max_length = 30)
    yt = models.CharField(default = "-",max_length = 30)
    link = models.CharField(default = "-",max_length = 30)
    team = models.CharField(default = "-",max_length = 30)

    picurl = models.TextField(default="")
    picname = models.TextField(default="")

    picurl2 = models.TextField(default="")
    picname2 = models.TextField(default="")
    #models.IntegerField()
    #models.CharField()

    site_set = models.CharField(default = "-",max_length = 30)
    tell = models.CharField(default = "-",max_length = 30)

    def __str__ (self):
        return self.site_set + " | " + str(self.pk)
