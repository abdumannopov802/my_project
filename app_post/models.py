from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE
    )
    text = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        reverse('postdetails', args=[str(self.pk)])