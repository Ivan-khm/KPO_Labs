class CreateTables:
    # Функция создания таблиц БД
    def create_table(self, connection, curs):
        # Создание таблицы предметов
        curs.execute("""CREATE TABLE subject
                            (id_subject INTEGER PRIMARY KEY, subject_name text, day_of_the_week text,
                             cabinet text, teacher text)
                         """)

        # Создание таблицы преподавателей
        curs.execute("""CREATE TABLE teachers
                                (id_teacher INTEGER PRIMARY KEY, full_name text, teach_subject text,
                                 count_subject_per_week text, count_student_subject text)
                             """)

        # Создание таблицы дней недели
        curs.execute("""CREATE TABLE days_week
                                    (id_days_week INTEGER PRIMARY KEY, day_name text, count_subj_per_day text)
                                 """)

        # Сохранение изменений
        connection.commit()

    # Функция добавления данных в таблицы БД
    def adding_data(self, connection, curs):
        # Данные для таблицы предметов
        data_sub = [('1', 'KPO', 'Saturday', 'D-614', 'Kurganskaya O.V.'),
                    ('2', 'KPO', 'Saturday', 'D-608', 'Kurganskaya O.V.'),
                    ('3', 'TPR', 'Wednesday', 'D-313', 'Ermakov A.A.'),
                    ('4', 'NPO', 'Thursday', 'D-218', 'Ermakov A.A.'),
                    ('5', 'ZPS', 'Tuesday', 'D-523', 'Krakovskii Y.M.'),
                    ('6', 'ZPS', 'Friday', 'A-208', 'Krakovskii Y.M.'),
                    ('7', 'TPR', 'Tuesday', 'A-511', 'Ermakov A.A.'),
                    ('8', 'OUD', 'Friday', 'D-618', 'Kirillova T.K.'),
                    ('9', 'AVS', 'Tuesday', 'D-614', 'Kashkavskii V.V.')]

        # Добавление данных в таблицу предметов
        curs.executemany("INSERT INTO subject VALUES (?, ?, ?, ?, ?)", data_sub)

        # Данные для таблицы преподавателей
        data_teach = [('1', 'Kurganskaya O.V.', 'KPO', '2', '18'),
                      ('2', 'Ermakov A.A.', 'TPR', '3', '14'),
                      ('3', 'Ermakov A.A.', 'NPO', '4', '12'),
                      ('4', 'Krakovskii Y.M.', 'ZPS', '1', '17'),
                      ('5', 'Kashkavskii V.V.', 'AVS', '2', '16')]

        # Добавление данных в таблицу преподавателей
        curs.executemany("INSERT INTO teachers VALUES (?, ?, ?, ?, ?)", data_teach)

        # Данные для таблицы дней недели
        data_day_week = [('1', 'Monday', '0'),
                         ('2', 'Tuesday', '3'),
                         ('3', 'Wednesday', '1'),
                         ('4', 'Thursday', '1'),
                         ('5', 'Friday', '2'),
                         ('6', 'Saturday', '2')]

        # Добавление данных в таблицу дней недели
        curs.executemany("INSERT INTO days_week VALUES (?, ?, ?)", data_day_week)

        # Сохранение изменений
        connection.commit()
 
