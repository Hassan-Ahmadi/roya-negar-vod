from django.urls import path
from .views import get_total_movie_watch_time, get_total_user_watch_time, get_latest_moment

app_name = "watchstats"

urlpatterns = [
    # path("", get_total_movie_watch_time),
    path("watch_time/slug/<str:slug>/", get_total_movie_watch_time),
    path("watch_time/user/<str:user>/", get_total_user_watch_time),
    path("latest_moment/user/<str:user>/slug/<str:slug>", get_latest_moment),    
]