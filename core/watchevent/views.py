from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import WatchEventSerializer
from rest_framework.decorators import api_view
from django.db import transaction

# Create your views here.

@csrf_exempt
@api_view(['POST'])
@transaction.atomic
def event_receiver(request):
    """ recieves json events from external service """
    if request.method == 'POST':
        serializer = WatchEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
