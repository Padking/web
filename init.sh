sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx_1_8_12.conf
sudo /etc/init.d/nginx restart

# Проверка правильности выполнения задания
curl http://localhost/uploads/proba.txt
