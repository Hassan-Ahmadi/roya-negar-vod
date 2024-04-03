# Design Decisions

## Initial Architecture

Based on the project document and its requirments, this project should be able to handle a high volume of events, so it seems that these events may grow eventually and some kind of load balencing might be required soon.

Without considering the load it seem that the below initial architecture would suffice:

![initial architecture](Initial%20Architecture.png "initial arch")

## Improved Architecture

But when high volume of events and realtime handeling of them is considered below elements seem logical to be added:

### Message Queue

A message queue to ensure no event is missed even with high volumes also allow for multiple consumer in the future that currenctly **RabbitMQ** is chosen

### Events Queueing service

A lightweight yet async service which has to get events and push them the queue. **FastApi + uvicorn** is chosen for its lightweightness and smooth async request handeling. This also helps seperation of conerns and modularity.

### User Request Handler Service

An async app in django to constanly consume events from the queue then process and store them and also handle user requests. For this project **Django + gunicorn** is chosen for its completeness, modularity and its strong ORM

### Database

As the payload has a fixed format a SQL db may work well for now, also the db should be capabale of handeling a large connection pool. For now **PostgreSQL** seems to be a strong choice

### Web Server

A reverse proxy is needed to ensure robust request redirection which at the moment **Nginx** is used

with the above description the architecture changes to:

![Improved Architecture](./Improved%20Architecture.png "Improved Architecture")

The above architecuture allow us to scale much easier, adding instances to consume event from events source or consume queued events from RabbitMQ using multiple instances of django or any other backend.

But based on the First law of software architecture *Every thing is a tradeoff* so although adding queue adds reliability to our architecture it also adds some overhead and may slightly slow down the processing time.

## Future Works

- [ ] Engancing the Event Queue using Kafka
- [ ] Handeling user request asyncrounesly using FastApi and deploying microserver
- [ ] Using disterbuted DB for scaling
- [ ] Based on the users traffic pattern a caching system can be added
