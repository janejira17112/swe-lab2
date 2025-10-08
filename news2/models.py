from django.db import models

# Create your models here.
class News2Post(models.Model):
    newstitle = models.CharField(max_length=200)
    newscontent = models.TextField()
