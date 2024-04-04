from django.contrib import admin
from .models import WatchEvent
# Register your models here.

@admin.register(WatchEvent)
class WatchEventAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user',
                    'slug',
                    'at',
                    'created_at',
                    )

    # -created_at means reverse order of created_at
    list_filter = ('slug', 'user')
    ordering = ('-created_at',)
    search_fields = ('user', 'slug')
