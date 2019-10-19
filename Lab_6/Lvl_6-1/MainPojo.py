class MainPojo(object):

    # Объявление переменных
    def __init__(self):
        self.Timetable = ''
    
    # Функция, возвращающая значение тега 'Timetable'
    @property
    def get_Timetable(self):
        return self.Timetable
   
    # Функция присваивания значения тегу 'Timetable'
    @get_Timetable.setter
    def get_Timetable(self, value):
        self.Timetable = value

    # Вывод в консоль полученных данных
    def toStringMainPojo(self):
        print("Class pojo [Timetable = " + self.Timetable + "]")
 
