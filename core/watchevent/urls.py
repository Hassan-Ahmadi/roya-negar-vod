from django.urls import path
from .views import event_receiver

app_name = "watchevent"

urlpatterns = [
    path("", event_receiver),
]
