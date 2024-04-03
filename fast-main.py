from fastapi import FastAPI
import pika

app = FastAPI()

@app.get("/")
async def put_event_in_queue():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='events')

    message = 'New event'
    channel.basic_publish(exchange='', routing_key='events', body=message)

    connection.close()

    return {"message": "Event added to the queue"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
