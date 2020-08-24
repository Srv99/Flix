from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=5000)
    path = models.CharField(max_length=100)
    datetime = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    datetime = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
