from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    location = models.CharField(max_length=128)
    gamer = models.CharField(max_length=128)



    def __str__(self):
        return self.title 

    def __str__(self):
        return self.location 

    def __str__(self):
        return self.gamer

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])