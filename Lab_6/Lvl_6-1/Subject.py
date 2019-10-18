class Subject(object):

    # Объявление переменных
    def __init__(self):
        self.name_sub = ''
        self.Day = ''
        self.Audience = ''

    @property
    def get_name_sub(self):
        return self.name_sub

    @get_name_sub.setter
    def get_name_sub(self, value):
        self.name_sub = value

    @property
    def get_day(self):
        return self.Day

    @get_day.setter
    def get_day(self, value):
        self.Day = value

    @property
    def get_audience(self):
        return self.Audience

    @get_audience.setter
    def get_audience(self, value):
        self.Audience = value

    # Вывод в консоль полученных данных
    def toStringSubject(self):
        print("[name_sub = " + self.name_sub + ", Day = " + self.Day + ", Audience = " + self.Audience + "]")
