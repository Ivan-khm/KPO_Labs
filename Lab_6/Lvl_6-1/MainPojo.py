class MainPojo(object):

    # Объявление переменных
    def __init__(self):
        self.Timetable = ''

    @property
    def get_Timetable(self):
        return self.Timetable

    @get_Timetable.setter
    def get_Timetable(self, value):
        self.Timetable = value

    # Вывод в консоль полученных данных
    def toStringMainPojo(self):
        print("[Timetable = " + self.Timetable + "]")
 
