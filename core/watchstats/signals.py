from django.db.models.signals import post_save
from django.dispatch import receiver
from watchevent.models import WatchEvent
from .models import UserWatchTime, LatestMomentWatched, MovieWatchTime

@receiver(post_save, sender=WatchEvent)
def update_latest_moment(sender, instance, created, **kwargs):
    """ updates last moment watched of a movie for a user whenever a new watchevent is recieved """
    if created:
        latest_moment_obj = LatestMomentWatched.objects.filter(user=instance.user, slug=instance.slug).first()
        if latest_moment_obj:
            latest_moment_obj.latest_moment += instance.at
            latest_moment_obj.save()
        else:            
            latest_moment_obj = LatestMomentWatched(user=instance.user, slug=instance.slug, latest_moment=instance.at)
            latest_moment_obj.save()

@receiver(post_save, sender=WatchEvent)
def update_user_watch_time(sender, instance, created, **kwargs):
    """ updates total watch time of a user whenever a new watchevent is recieved """
    if created:
        user_watch_time_obj = UserWatchTime.objects.filter(user=instance.user).first()
        if user_watch_time_obj:
            user_watch_time_obj.total_watch_time += instance.at
            user_watch_time_obj.save()
        else:                
            user_watch_time_obj = UserWatchTime(user=instance.user, total_watch_time=instance.at)
            user_watch_time_obj.save()

@receiver(post_save, sender=WatchEvent)
def update_movie_watch_time(sender, instance, created, **kwargs):
    """ updates total watch time of a movies whenever a new watchevent is recieved """
    if created:
        movie_watch_time_obj = MovieWatchTime.objects.filter(slug=instance.slug).first()
        if movie_watch_time_obj:
            movie_watch_time_obj.total_watch_time += instance.at
            movie_watch_time_obj.save()
        else:
            movie_watch_time_obj = MovieWatchTime(slug=instance.slug, total_watch_time=instance.at)
            movie_watch_time_obj.save()
