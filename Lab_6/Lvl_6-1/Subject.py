class Subject(object):

    # Объявление переменных
    def __init__(self):
        self.name_sub = ''
        self.Day = ''
        self.Audience = ''

    # Функция, возвращающая значение тега 'name_sub'
    @property
    def get_name_sub(self):
        return self.name_sub

    # Функция присваивания значения тегу 'name_sub'
    @get_name_sub.setter
    def get_name_sub(self, value):
        self.name_sub = value

    # Функция, возвращающая значение тега 'Day'
    @property
    def get_day(self):
        return self.Day

    # Функция присваивания значения тегу 'Day'
    @get_day.setter
    def get_day(self, value):
        self.Day = value

    # Функция, возвращающая значение тега 'Audience'
    @property
    def get_audience(self):
        return self.Audience

    # Функция присваивания значения тегу 'Audience'
    @get_audience.setter
    def get_audience(self, value):
        self.Audience = value

    # Вывод в консоль полученных данных
    def toStringSubject(self):
        print("Class pojo [name_sub = " + self.name_sub + ", Day = " + self.Day + ", Audience = " + self.Audience + "]")
  
