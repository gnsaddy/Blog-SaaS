#!/bin/sh


echo "**************** waiting for server volume ****************"
until cd /usr/src/app
do
    echo "**************** Waiting for server volume ****************"
done

date +'FORMAT'
### mm/dd/yyyy ###
date +'%m/%d/%Y'
## Time in 12 hr format ###
date +'%r'
## backup dir format ##
migrate_time=$(date +'%m/%d/%Y')


echo "**************** migrating ****************"
python ./manage.py migrate --noinput --run-syncdb

echo "**************** running migrations ****************"
python ./manage.py makemigrations

python ./manage.py migrate --noinput --run-syncdb

echo "**************** collecting static ****************"
python ./manage.py collectstatic --noinput

echo "**************** starting gunicorn ****************"
gunicorn --bind 0.0.0.0:8008 cms_ms.wsgi --workers=2 --threads=4 --log-level debug --reload --timeout=300 
echo "**************** gunicorn running ****************"