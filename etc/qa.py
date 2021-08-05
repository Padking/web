# gunicorn configuration file for "qa" django application

pythonpath = '/home/box/web/ask/'  # путь до дефолтного django-приложения
bind = "0.0.0.0:8000"
workers = 4
