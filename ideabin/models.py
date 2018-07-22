from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ideas')
    title = models.CharField(blank=True, null=True, max_length=255)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='ideabin_images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'ideas'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ideabin:detail", kwargs={'pk' : self.pk})
        