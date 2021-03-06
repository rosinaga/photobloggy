from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #photo = models.
    description = models.TextField()
    emotion = models.CharField(max_length=50)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
