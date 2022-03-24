from django.db import models
from django.urls import reverse


class Post(models.Model):
    game = models.CharField(max_length=128)
    text = models.TextField()
    location = models.CharField(max_length=128)
    gamer = models.CharField(max_length=128)


    def __str__(self):
        return self.game

    def __repr__(self):
        return "<%s - %s By: %s>" (self.game, self.location, self.gamer) 

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])