# gunicorn configuration file for "hello" python application

pythonpath = '/home/box/web/'  # путь до приложения
bind = "0.0.0.0:8080"
workers = 4
