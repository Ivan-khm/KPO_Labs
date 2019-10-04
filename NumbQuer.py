from GetInf import GetInf


class NumbQuery:
    # Ввод данных для первого запроса
    def first_query(self, curs):
        day = input("Enter the day of the week: ")
        numb_cabinet = input("Enter cabinet number: ")
        obj_gi = GetInf()
        a = obj_gi.get_information_first_query(day, numb_cabinet, curs)
        return a

    # Ввод данных для второго запроса
    def second_query(self, curs):
        day = input("Enter the day of the week: ")
        obj_gi = GetInf()
        a = obj_gi.get_information_second_query(day, curs)
        return a

    # Ввод данных для третьего запроса
    def third_query(self, curs):
        count = input("Enter count of subjects: ")
        obj_gi = GetInf()
        a = obj_gi.get_information_third_query(count, curs)
        return a

    # Ввод данных для четвертого запроса
    def fourth_query(self, curs):
        count = input("Enter count of busy classrooms: ")
        obj_gi = GetInf()
        a = obj_gi.get_information_fourth_query(count, curs)
        return a
