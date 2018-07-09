from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")
    title = models.CharField(blank=True, null=True, max_length=255)
    body = models.TextField(blank=True, null=True)
    entry_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.title

