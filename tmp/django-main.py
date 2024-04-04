import asyncio
import pika
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.conf import settings
from event_reader.models import Event

class RabbitMQConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBITMQ_HOST))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=settings.RABBITMQ_QUEUE)

        await self.accept()

        def callback(ch, method, properties, body):
            event = Event(data=body.decode())
            event.save()

        self.channel.basic_consume(queue=settings.RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

    async def disconnect(self, close_code):
        self.channel.stop_consuming()
        self.connection.close()
