from django.contrib import admin
from .models import LatestMomentWatched, MovieWatchTime, UserWatchTime
# Register your models here.


@admin.register(UserWatchTime)
class UserWatchTimeAdmin(admin.ModelAdmin):
    """ admin class to modify fields in django admin panel """
    
    date_hierarchy = 'created_at'
    list_display = ('user',
                    'total_watch_time',
                    'created_at',
                    )

    list_filter = ('user', 'total_watch_time')
    ordering = ('-created_at',)
    search_fields = ('user',)


@admin.register(MovieWatchTime)
class MovieWatchTimeAdmin(admin.ModelAdmin):
    """ admin class to modify fields in django admin panel """
    
    date_hierarchy = 'created_at'
    list_display = ('slug',
                    'total_watch_time',
                    'created_at',
                    )
    list_filter = ('slug', 'total_watch_time')
    ordering = ('-created_at',)
    search_fields = ('slug',)
    

@admin.register(LatestMomentWatched)
class LatestMomentWatchedAdmin(admin.ModelAdmin):
    """ admin class to modify fields in django admin panel """
    
    date_hierarchy = 'created_at'
    list_display = ('user',
                    'slug',
                    'latest_moment',
                    'created_at',
                    )

    list_filter = ('user', 'slug')
    ordering = ('-created_at',)
    search_fields = ('user', 'slug')




