From python:3.11.4-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./core /app/

# It will be executed in docker compose
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
