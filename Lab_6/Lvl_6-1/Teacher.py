class Teacher(object):

    # Объявление переменных
    def __init__(self):
        self.full_name = ''
        self.Sub_teach = ''
        self.Count_sub_per_week = ''
        self.Count_students = ''

    # Функция, возвращающая значение тега 'full_name'
    @property
    def get_full_name(self):
        return self.full_name

    # Функция присваивания значения тегу 'full_name'
    @get_full_name.setter
    def get_full_name(self, value):
        self.full_name = value

    # Функция, возвращающая значение тега 'Sub_teach'
    @property
    def get_sub_teach(self):
        return self.Sub_teach

    # Функция присваивания значения тегу 'Sub_teach'
    @get_sub_teach.setter
    def get_sub_teach(self, value):
        self.Sub_teach = value

    # Функция, возвращающая значение тега 'Count_sub_per_week''
    @property
    def get_count_sub_per_week(self):
        return self.Count_sub_per_week

    # Функция присваивания значения тегу 'Count_sub_per_week'
    @get_count_sub_per_week.setter
    def get_count_sub_per_week(self, value):
        self.Count_sub_per_week = value

    # Функция, возвращающая значение тега 'Count_students'
    @property
    def get_count_students(self):
        return self.Count_students

    # Функция присваивания значения тегу 'Count_students'
    @get_count_students.setter
    def get_count_students(self, value):
        self.Count_students = value

    # Вывод в консоль полученных данных
    def toStringTeacher(self):
        print("[full_name = " + self.full_name,  ", Sub_teach = " + self.Sub_teach + ", "
              "Count_sub_per_week = " + self.Count_sub_per_week + ", Count_students = " + self.Count_students + " ]")
 
