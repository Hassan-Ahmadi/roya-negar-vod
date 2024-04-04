from django.db import models

class WatchEvent(models.Model):
    user_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    time_spent = models.IntegerField()

# Perform the queries:
# Perform the queries:
from django.db.models import Sum

last_moment_watched = WatchEvent.objects.filter(user_name='desired_user', slug='desired_slug').aggregate(last_moment_watched=Sum('time_spent'))

# Total user watch time
total_user_watch_time = WatchEvent.objects.filter(user_name='desired_user').aggregate(total_user_watch_time=Sum('time_spent'))

# Total movie watch time
total_movie_watch_time = WatchEvent.objects.filter(slug='desired_slug').aggregate(total_movie_watch_time=Sum('time_spent'))

