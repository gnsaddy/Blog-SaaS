#!/bin/sh


echo "**************** waiting for server volume ****************"
until cd /usr/src/app
do
    echo "**************** Waiting for server volume ****************"
done

echo "**************** Waiting for db to be ready ****************"

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "**************** migrating ****************"
python ./manage.py migrate

echo "**************** running migrations ****************"
python ./manage.py makemigrations

python ./manage.py migrate

echo "**************** collecting static ****************"
python ./manage.py collectstatic --noinput

echo "**************** starting gunicorn ****************"
gunicorn --bind 0.0.0.0:8008 multi_tenant_blog.wsgi --workers 2 --threads 4 --log-level debug --reload
echo "**************** gunicorn running ****************"