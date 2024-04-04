from django.db.models.signals import post_save
from django.dispatch import receiver
from watchevent.models import WatchEvent
from .models import UserWatchTime, LatestMomentWatched, MovieWatchTime

def update_last_moment(instance, **kwargs):
    """ updates last moment watched of a movie for a user whenever a new watchevent is recieved """
    latest_moment_obj = LatestMomentWatched.objects.filter(user=instance.user, slug=instance.slug).first()
    if latest_moment_obj:            
        latest_moment_obj.last_moment += instance.at
        latest_moment_obj.save()
    else:            
        latest_moment_obj = LatestMomentWatched(user=instance.user, slug=instance.slug, last_moment=instance.at)
        latest_moment_obj.save()

def update_user_watch_time(instance, **kwargs):
    """ updates total watch time of a user whenever a new watchevent is recieved """
    user_watch_time_obj = UserWatchTime.objects.filter(user=instance.user).first()
    if user_watch_time_obj:
        user_watch_time_obj.total_watch_time += instance.at
        user_watch_time_obj.save()
    else:                
        user_watch_time_obj = UserWatchTime(user=instance.user, total_watch_time=instance.at)
        user_watch_time_obj.save()

def update_movie_watch_time(instance, **kwargs):
    """ updates total watch time of a movies whenever a new watchevent is recieved """
    movie_watch_time_obj = MovieWatchTime.objects.filter(slug=instance.slug).first()
    if movie_watch_time_obj:
        movie_watch_time_obj.total_watch_time += instance.at
        movie_watch_time_obj.save()
    else:
        movie_watch_time_obj = MovieWatchTime(slug=instance.slug, total_watch_time=instance.at)
        movie_watch_time_obj.save()

@receiver(post_save, sender=WatchEvent)
def update_fields(sender, instance, created, **kwargs):
    """ recieves post_save signal from watchevent model to update other tables fields"""
    if created:
        print(' --------------------------------------- ')
        print("Signal Called!!!!!!")
        print(' --------------------------------------- ')
        update_last_moment(instance=instance)
        update_user_watch_time(instance=instance)
        update_movie_watch_time(instance=instance)
