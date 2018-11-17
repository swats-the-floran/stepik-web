#sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
﻿sudo /etc/init.d/mysql start﻿
sudo apt-get update
sudo apt-get install python3.5
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3.5 get-pip.py