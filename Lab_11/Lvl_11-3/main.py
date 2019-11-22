class Subject(object):
    # Субъект
    def __init__(self):
        self._data = None
        self._observers = set()

    def attach(self, observer):
        # подписаться на оповещение
        if not isinstance(observer, ObserverBase):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):
        # отписаться от оповещения
        self._observers.remove(observer)

    def get_data(self):
        # Получение информации
        return self._data

    def set_data(self, data):
        # Установка информации
        self._data = data
        self.notify(data)

    def notify(self, data):
        # уведомить всех наблюдателей о событии
        for observer in self._observers:
            observer.update(data)


class ObserverBase(object):
    # Абстрактный наблюдатель
    def update(self, data):
        raise NotImplementedError()


class Observer(ObserverBase):
    # Наблюдатель
    def __init__(self, name):
        self._name = name

    def update(self, data):
        if self._name == "Подписчик 1":
            print('%s: %s' % (self._name, data[0]))
        elif self._name == "Подписчик 2":
            print('%s: %s' % (self._name, data[1]))


subject = Subject()
subject.attach(Observer('Подписчик 1'))
subject.attach(Observer('Подписчик 2'))
subject.set_data(['Журнал', 'Газета'])
 
