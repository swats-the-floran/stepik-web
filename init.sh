#pip3 uninstall django
#pip3 uninstall gunicorn
apt-get update
apt-get install -f python3.5
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3.5 get-pip.py
# pip install django
# pip install gunicorn
rm /etc/nginx/sites-enabled/default
cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart
cp /home/box/web/etc/guni*   /etc/gunicorn.d/
cp edinorogs/gunicorn-debian /usr/sbin/
cp edinorogs/gunicorn /usr/bin/
cp edinorogs/gunicorn_* /usr/sbin/
/etc/init.d/gunicorn restart