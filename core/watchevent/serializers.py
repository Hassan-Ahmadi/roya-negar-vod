from rest_framework import serializers
from .models import WatchEvent

class WatchEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchEvent
        fields = ['user', 'slug', 'at']
