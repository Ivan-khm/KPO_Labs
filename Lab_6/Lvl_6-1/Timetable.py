class Timetable(object):

    # Объявление переменных
    def __init__(self):
        self.Subject = ''
        self.Teacher = ''

    @property
    def get_subject(self):
        return self.Subject

    @get_subject.setter
    def get_subject(self, value):
        self.Subject = value

    @property
    def get_teacher(self):
        return self.Teacher

    @get_teacher.setter
    def get_teacher(self, value):
        self.Teacher = value

    # Вывод в консоль полученных данных
    def toStringTimetable(self):
        print("[Teacher = " + self.Teacher + ", Subject = " + self.Subject + "]")
 
