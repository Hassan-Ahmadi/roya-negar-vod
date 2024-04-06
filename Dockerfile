From python:3.11.4-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./core /app/

# Run Django migrations
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# # Collect static files
# RUN python manage.py collectstatic --noinput


# Create superuser if it doesn't exist
# RUN python -c "import django; django.setup(); \
#                from django.contrib.auth.models import User; \
#                User.objects.filter(username='admin').exists() or \
#                User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
               