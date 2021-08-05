import socket
import selectors # модная оболочка в виде модуля - слой абстрактной логики над модулем select, выполняет мониторинг над файлам в общем смысле
# у каждой ОС свой селектор; в Windows - selectors.SelectSelector

""" #3
Этот скрипт есть модификация #2 part 2.
Асинхронная работа с двумя клиентами в одном потоке за счёт наличия управляющего кода на коллбэках
Отличие заключается в использовании selectors и особенностях использования функций этого модуля
Для простоты, написанный код носит название "асинхронности на колбэках"
"""

selector = selectors.DefaultSelector()

def server():
    """Определяет серверный сокет
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    server_socket.bind(('localhost', 5000)) 
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection) # регистрация файлового объекта, интересующего события и связанные данные


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket):
    request = client_socket.recv(4096)
    
    if request:
        response = 'Hello world\n'.encode() #ответ сервера
        client_socket.send(response) 
    else:
        selector.unregister(client_socket) # снимаем с реги
        client_socket.close() # закрываем, т.к. клиент не шлёт запросов
    

def event_loop():
    while True:
        events = selector.select() # (key, events) один кортеж на один зареганый объект, где events - битовая маска события, чтения/записи
        # key - Selectorkey instance - именованный кортеж (namedtuple)
        """ Рассматриваем объект Selectorkey"""
        for key, _ in events: # фишка асинхронности на колбэках
            callback = key.data # сущность колбэка
            callback(key.fileobj) # fileobj - сокет


#if __name__ == 'main':
#    accept_connection(server_socket)
server()
event_loop()
    