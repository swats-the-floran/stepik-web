﻿# dont forget that in gunicorn configs python 3.5 should be used
# all changed filed i added to an "edinorogs" directory
apt-get update
#apt-get -y install libffi-dev
# for python 3.5
apt-get install -f python3.5
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3.5 get-pip.py
# installing openssl of acceptable version
#git clone https://github.com/swats-the-floran/stepik-python37
#cd stepik-python37/openssl-1.1.0j/
#sudo make install
#sudo ldconfig
#cd ../../
# installing python3.7.1
#cd stepik-python37/Python-3.7.1/
#sudo -H make install
#cd ../../
# installing libraries
pip install django
pip install gunicorn
# configs
rm /etc/nginx/sites-enabled/default
cp web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
cp web/etc/guni*   /etc/gunicorn.d/
cp edinorogs/gunicorn-debian /usr/sbin/
cp edinorogs/gunicorn /usr/bin/
cp edinorogs/gunicorn_* /usr/sbin/
# launching and relaunching services
sudo /etc/init.d/mysql start
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restartc
# other stuff
mysql -u root -e "CREATE DATABASE stepik CHARACTER SET utf8;"
./manage.py makemigrations
./manage.py migrate