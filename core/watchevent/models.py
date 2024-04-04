from django.db import models

# Create your models here.

class WatchEvent(models.Model):
    user = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    at = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user}-{self.slug}-{self.at}'

    class Meta:
        ordering = ['created_at']