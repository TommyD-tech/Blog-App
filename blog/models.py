
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title[:15]

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model): # new
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') 
    comment = models.CharField(max_length=140, null=True, blank=True, default='DEFAULT VALUE') 
    author = models.ForeignKey( 
        get_user_model(), 
        on_delete=models.CASCADE, 
        related_name='comments',
    )


    def __str__(self): 
        return self.comment

    def get_absolute_url(self):
        return reverse('post_detail')

    
