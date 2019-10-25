import threading
import random


# функция первого туннеля
def first_tunnel(n, event_for_wait):
    print(n, ": заехал в 1 туннель")
    event_for_wait.wait(random.randint(2, 5))  # остановка события на время от 2 до 5 секунд
    print(n, ": выехал из 1 туннеля\n")
    event_for_wait.set()  # установка флага на true


# функция второго туннеля
def second_tunnel(n, event_for_wait):
    print(n, ": заехал во 2 туннель")
    event_for_wait.wait(random.randint(2, 5))  # остановка события на время от 2 до 5 секунд
    print(n, ": выехал из 2 туннеля\n")
    event_for_wait.set()  # установка флага на true


# инициализация событий
e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()
e4 = threading.Event()
e5 = threading.Event()

# инициализация потоков t1 и t2
t1 = threading.Thread(target=first_tunnel, args=("первый поезд", e1))
t2 = threading.Thread(target=second_tunnel, args=("второй поезд", e2))
t1.start()  # запуск потока t1
t2.start()  # запуск потока t2

# дерево условий для очереди (синхронизации) потоков
# (ручная установка очереди для 5 поездов(потоков) и 2 туннелей(функций))
# цикл пока 1 и 2 события работают
while not e1.is_set() and not e2.is_set():
    # ничего не делать
    pass
# если 1 событие закончилось
if e1.is_set():
    # инициализация и запуск 3 потока(поезда) в 1 туннель
    t3 = threading.Thread(target=first_tunnel, args=("третий поезд", e3))
    t3.start()
    # цикл пока 2 и 3 события работают
    while not e2.is_set() and not e3.is_set():
        pass
    # если 2 событие закончилось
    if e2.is_set():
        # инициализация и запуск 4 потока(поезда) во 2 туннель
        t4 = threading.Thread(target=second_tunnel, args=("четвертый поезд", e4))
        t4.start()
        # цикл пока 4 и 3 события работают
        while not e4.is_set() and not e3.is_set():
            pass
        # если 3 событие закончилось
        if e3.is_set():
            # инициализация и запуск 5 потока(поезда) в 1 туннель
            t5 = threading.Thread(target=first_tunnel, args=("пятый поезд", e5))
            t5.start()
        # если 4 событие закончилось
        elif e4.is_set():
            # инициализация и запуск 5 потока(поезда) во 2 туннель
            t5 = threading.Thread(target=second_tunnel, args=("пятый поезд", e5))
            t5.start()
    # если 3 событие закончилось
    elif e3.is_set():
        # инициализация и запуск 4 потока(поезда) в 1 туннель
        t4 = threading.Thread(target=first_tunnel, args=("четвертый поезд", e4))
        t4.start()
        # цикл пока 4 и 2 события работают
        while not e4.is_set() and not e2.is_set():
            pass
        # если 4 событие закончилось
        if e4.is_set():
            # инициализация и запуск 5 потока(поезда) в 1 туннель
            t5 = threading.Thread(target=first_tunnel, args=("пятый поезд", e5))
            t5.start()
        # если 2 событие закончилось
        elif e2.is_set():
            # инициализация и запуск 5 потока(поезда) во 2 туннель
            t5 = threading.Thread(target=second_tunnel, args=("пятый поезд", e5))
            t5.start()

# если 2 событие закончилось
elif e2.is_set():
    # инициализация и запуск 3 потока(поезда) во 2 туннель
    t3 = threading.Thread(target=second_tunnel, args=("третий поезд", e3))
    t3.start()
    # цикл пока 1 и 3 события работают
    while not e1.is_set() and not e3.is_set():
        pass
    # если 1 событие закончилось
    if e1.is_set():
        # инициализация и запуск 4 потока(поезда) в 1 туннель
        t4 = threading.Thread(target=first_tunnel, args=("четвертый поезд", e4))
        t4.start()
        # цикл пока 4 и 3 события работают
        while not e4.is_set() and not e3.is_set():
            pass
        # если 3 событие закончилось
        if e3.is_set():
            # инициализация и запуск 5 потока(поезда) во 2 туннель
            t5 = threading.Thread(target=second_tunnel, args=("пятый поезд", e5))
            t5.start()
        # если 4 событие закончилось
        elif e4.is_set():
            # инициализация и запуск 5 потока(поезда) в 1 туннель
            t5 = threading.Thread(target=first_tunnel, args=("пятый поезд", e5))
            t5.start()
    # если 3 событие закончилось
    elif e3.is_set():
        # инициализация и запуск 4 потока(поезда) во 2 туннель
        t4 = threading.Thread(target=second_tunnel, args=("четвертый поезд", e4))
        t4.start()
        # цикл пока 1 и 4 события работают
        while not e1.is_set() and not e4.is_set():
            pass
        # если 1 событие закончилось
        if e1.is_set():
            # инициализация и запуск 5 потока(поезда) в 1 туннель
            t5 = threading.Thread(target=first_tunnel, args=("пятый поезд", e5))
            t5.start()
        # если 4 событие закончилось
        elif e4.is_set():
            # инициализация и запуск 5 потока(поезда) во 2 туннель
            t5 = threading.Thread(target=second_tunnel, args=("пятый поезд", e5))
 
