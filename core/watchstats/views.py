from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
from .models import LatestMomentWatched, MovieWatchTime, UserWatchTime
from .serializers import LatestMomentWatchedSerializer, MovieWatchTimeSerializer, UserWatchTimeSerializer
# Create your views here.


@csrf_exempt
@api_view(['GET'])
def get_total_movie_watch_time(request, slug):
    """
    Get total watch time of a movie in seconds by its slug
    """
    try:
        movie_watch_time = MovieWatchTime.objects.get(slug=slug)
    
    except MovieWatchTime.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
            serializer = MovieWatchTimeSerializer(movie_watch_time)
            return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def get_total_user_watch_time(request, user):
    """
    Get total time a user has watched all movies
    """
    try:
        user_watch_time = UserWatchTime.objects.get(user=user)
    
    except UserWatchTime.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
            serializer = UserWatchTimeSerializer(user_watch_time)
            return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def get_latest_moment(request, user, slug):
    """
    Get latest moment of a movie for a specific user
    """
    try:
        latest_moment_watched = LatestMomentWatched.objects.get(user=user, slug=slug)
    
    except LatestMomentWatched.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
            serializer = LatestMomentWatchedSerializer(latest_moment_watched)
            return Response(serializer.data)
