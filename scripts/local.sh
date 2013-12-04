#!/bin/bash
set -e
# vars
ADMIN_USER='admin'
ADMIN_PASSWORD='ad2&min3'
ADMIN_EMAIL='your_email@example.com'
SITENAME="localhost:8000"
PYTHON="env/bin/python"
PROJECT="{{ project_name }}"
set -x
# virtualenv
if [ ! -d env ]; then
    virtualenv --no-site-packages env
fi
# requirements.txt
env/bin/pip install -r requirements/local.txt
# DB(sqlite)
rm -f dev.db
# syncdb and South --migrate
$PYTHON $PROJECT/manage.py syncdb --migrate --noinput
# admin account
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')" | $PYTHON $PROJECT/manage.py shell
# runserver
$PYTHON $PROJECT/manage.py runserver
