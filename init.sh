# don't forget that in gunicorn configs python 3.5 should be used
# all changed filed i added to an "edinorogs" directory
sudo apt-get update
sudo apt-get -f install libffi-dev libssl-dev
# for python 3.5
#apt-get install -f python3.5
#curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
#python3.5 get-pip.py
#installing openssl of acceptable version
git clone https://github.com/swats-the-floran/stepik-python37
cd stepik-python37/openssl-1.1.0j/
sudo make install
sudo ldconfig
cd ../../
# installing python3.7.1
cd stepik-python37/Python-3.7.1/
sudo -H make install
cd ../../
# installing libraries
sudo -H pip3.7 install django
sudo -H pip3.7 install gunicorn
# configs
sudo rm /etc/nginx/sites-enabled/default
sudo cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo cp /home/box/web/etc/guni*   /etc/gunicorn.d/
sudo cp edinorogs/gunicorn-debian /usr/sbin/
sudo cp edinorogs/gunicorn /usr/bin/
sudo cp edinorogs/gunicorn_* /usr/sbin/
# launching and relaunching services
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restartc
