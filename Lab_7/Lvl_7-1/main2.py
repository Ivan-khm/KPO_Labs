import threading
import random


# функция туннеля
def tunnel(n, event_for_wait, event_for_set):
    event_for_wait.wait()  # ожидание события
    event_for_wait.clear()  # установка флага на false (потоки блокируются, пока не будет вызван метод set())
    print(n, ": заехал в 1 туннель")
    event_for_wait.wait(random.randint(1, 5))  # остановка события на время от 2 до 5 секунд
    print(n, ": выехал из 1 туннеля\n")
    event_for_set.set()  # установка флага на true


# инициализация событий
e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()
e4 = threading.Event()
e5 = threading.Event()

# инициализация потоков
t1 = threading.Thread(target=tunnel, args=("первый поезд", e1, e2))
t2 = threading.Thread(target=tunnel, args=("второй поезд", e2, e3))
t3 = threading.Thread(target=tunnel, args=("третий поезд", e3, e4))
t4 = threading.Thread(target=tunnel, args=("четвертый поезд", e4, e5))
t5 = threading.Thread(target=tunnel, args=("пятый поезд", e5, e1))

# запуск потоков
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

e1.set()  # установка флага на true

# присоединение потоков к основному потоку
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
 
