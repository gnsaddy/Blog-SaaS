docker-compose -f docker-compose.yml exec cms python manage.py migrate --noinput
docker-compose -f docker-compose.yml exec cms python manage.py makemigrations


docker-compose -f docker-compose.yml exec web python manage.py createsuperuser