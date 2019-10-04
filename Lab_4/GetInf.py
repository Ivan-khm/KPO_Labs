
class GetInf:
    # Получение данных из БД по введенным данным первого запроса
    def get_information_first_query(self, day, numb_cabinet, curs):
        sql = "SELECT full_name, teach_subject, count_subject_per_week, count_student_subject" \
              " FROM teachers, subject WHERE subject.day_of_the_week=? AND" \
              " subject.cabinet=? AND teachers.full_name = subject.teacher"
        curs.execute(sql, ["%s" % day, "%s" % numb_cabinet])
        return curs.fetchall()

    # Получение данных из БД по введенным данным второго запроса
    def get_information_second_query(self, day, curs):
        sql = "SELECT full_name, teach_subject, count_subject_per_week, count_student_subject" \
              " FROM teachers, subject WHERE NOT (subject.day_of_the_week=?) AND" \
              " (teachers.full_name = subject.teacher)"
        curs.execute(sql, ["%s" % day])
        return curs.fetchall()

    # Получение данных из БД по введенным данным третьего запроса
    def get_information_third_query(self, count, curs):
        sql = "SELECT day_name FROM days_week WHERE count_subj_per_day=?"
        curs.execute(sql, ["%s" % count])
        return curs.fetchall()

    # Получение данных из БД по введенным данным четвертого запроса
    def get_information_fourth_query(self, count, curs):
        sql = "SELECT day_name FROM days_week WHERE count_subj_per_day=?"
        curs.execute(sql, ["%s" % count])
        return curs.fetchall()
 
