from django.db import models

# Create your models here.

class UserWatchTime(models.Model):    
    user = models.CharField(max_length=255, unique=True)    
    total_watch_time = models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']


class MovieWatchTime(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    total_watch_time = models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

class LatestMomentWatched(models.Model):
    user = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    latest_moment = models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        unique_together = ['user', 'slug']
