sudo ln -s /home/box/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart

# Проверка правильности выполнения п.3 задания
gunicorn hello:app
curl http://localhost/?a=1&a=2&b=3
