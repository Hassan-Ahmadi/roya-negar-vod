from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import WatchEventSerializer
from django.db import transaction

# Create your views here.

@csrf_exempt
@transaction.atomic
def event_receiver(request):
    """ recieves json events from external service """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WatchEventSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            print(instance.user, instance.slug, instance.at)

            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
