#!/usr/bin/env bash
echo "This script downloads postgis and installs all needed apt-get libs"
virtualenv -p python3 env
source ./env/bin/activate
pip install -r ./requirements.txt
cd task
python manage.py migrate
python manage.py loaddata initial.json
echo "Superuser credentials: admin/admin"