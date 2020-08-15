sudo ln -s /home/box/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart

# Проверка правильности выполнения п.3 задания
gunicorn -c /etc/gunicorn.d/hello.py hello:app
curl http://localhost:8080/?a=1&a=2&b=3
# Завершена с ошибкой:
"""
Starting Gunicorn workers                                                    
Traceback (most recent call last):                                              
  File "/usr/sbin/gunicorn-debian", line 218, in <module>                       
    sys.exit(main())                                                            
  File "/usr/sbin/gunicorn-debian", line 84, in main                            
    module = imp.load_source(filename, filename)                                
IOError: [Errno 2] No such file or directory
"""
