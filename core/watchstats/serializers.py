from rest_framework import serializers
from .models import UserWatchTime, MovieWatchTime, LatestMomentWatched

class UserWatchTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWatchTime
        fields = ['user', 'total_watch_time']

class MovieWatchTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieWatchTime
        fields = ['slug', 'total_watch_time']

class LatestMomentWatchedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestMomentWatched
        fields = ['user', 'slug', 'latest_moment']
