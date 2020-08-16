sudo rm -rf /etc/nginx/sites-enabled/default
# sudo rm -rf /etc/gunicorn.d/django.example
# sudo rm -rf /etc/gunicorn.d/wsgi.example

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx_1_9_11.conf
# sudo ln -sf /home/box/web/etc/hello.conf /etc/gunicorn.d/hello

sudo /etc/init.d/nginx restart
# sudo /etc/init.d/gunicorn restart
