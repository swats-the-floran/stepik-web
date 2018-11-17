/etc/init.d/mysql start﻿
apt-get update
apt-get install python3.5
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3.5 get-pip.py
pip install django
pip install gunicorn
cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart
cp /home/box/web/etc/guni*   /etc/gunicorn.d/
#/etc/init.d/gunicorn restart