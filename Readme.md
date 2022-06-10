docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput


 find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf