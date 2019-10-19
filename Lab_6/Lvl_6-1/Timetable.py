class Timetable(object):

    # Объявление переменных
    def __init__(self):
        self.Subject = ''
        self.Teacher = ''

    # Функция, возвращающая значение тега 'Subject'
    @property
    def get_subject(self):
        return self.Subject

    # Функция присваивания значения тегу 'Subject'
    @get_subject.setter
    def get_subject(self, value):
        self.Subject = value

    # Функция, возвращающая значение тега 'Teacher'
    @property
    def get_teacher(self):
        return self.Teacher

    # Функция присваивания значения тегу 'Teacher'
    @get_teacher.setter
    def get_teacher(self, value):
        self.Teacher = value

    # Вывод в консоль полученных данных
    def toStringTimetable(self):
        print("[Teacher = " + self.Teacher + ", Subject = " + self.Subject + "]")
 
