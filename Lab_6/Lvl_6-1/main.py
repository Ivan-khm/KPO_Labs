# Импортирование класса 'MainPojo' из файла 'MainPojo'
from MainPojo import MainPojo
# Импортирование класса 'Timetable' из файла 'Timetable'
from Timetable import Timetable
# Импортирование класса 'Subject' из файла 'Subject'
from Subject import Subject
# Импортирование класса 'Teacher' из файла 'Teacher'
from Teacher import Teacher
# Импортирование модуля 'pickle' для сериализации и десериализации объектов
import pickle


if __name__ == '__main__':
    # Создание объекта класса MainPojo
    Mp = MainPojo()
    # Передача значения 'Timetable' в метод 'get_Timetable'
    Mp.get_Timetable = "Timetable"

    # Создание объекта класса Timetable
    Tt = Timetable()
    # Передача значения 'Subject' в метод 'get_subject' класса 'Timetable'
    Tt.get_subject = "Subject"
    # Передача значения 'Teacher' в метод 'get_teacher' класса 'Timetable'
    Tt.get_teacher = "Teacher"

    # Создание объекта класса Subject
    Su = Subject()
    # Передача значения 'TPR' в метод 'get_name_sub' класса 'Subject'
    Su.get_name_sub = 'TPR'
    # Передача значения 'Monday' в метод 'get_day' класса 'Subject'
    Su.get_day = 'Monday'
    # Передача значения 'D-514' в метод 'get_audience' класса 'Subject'
    Su.get_audience = 'D-514'

    # Создание объекта класса Teacher
    Te = Teacher()
    # Передача значения 'Ermakov A.A.' в метод 'get_full_name' класса 'Teacher'
    Te.get_full_name = 'Ermakov A.A.'
    # Передача значения 'TPR' в метод 'get_sub_teach' класса 'Teacher'
    Te.get_sub_teach = 'TPR'
    # Передача значения '2' в метод 'get_count_sub_per_week' класса 'Teacher'
    Te.get_count_sub_per_week = '2'
    # Передача значения '16' в метод 'get_count_students' класса 'Teacher'
    Te.get_count_students = '16'

    # Вывод в консоль текста 'Полученный POJO класс'
    print("\nПолученный POJO класс:\n")
    # Вызов метода 'toStringMainPojo' класса 'MainPojo'
    Mp.toStringMainPojo()
    # Вызов метода 'toStringTimetable' класса 'Timetable'
    Tt.toStringTimetable()
    # Вызов метода 'toStringSubject' класса 'Subject'
    Su.toStringSubject()
    # Вызов метода 'toStringTeacher' класса 'Teacher'
    Te.toStringTeacher()
    # Вывод в консоль знака '*' 100 раз
    print("*" * 100)

    # Присвоение переменной 'output_file' названия файла 'pickle.pickle'
    output_file = 'pickle.pickle'
    # Открытие файла 'pickle.pickle' для записи
    with open(output_file, 'wb') as file:
        # Запись полученных данных в файл
        pickle.dump((Mp, Tt, Su, Te), file)

    # Передача значения 'Friday' в метод 'get_day' класса 'Subject'
    Su.get_day = 'Friday'

    # Вывод в консоль текста 'Обновленный POJO с изменённым аргументом:'
    print("\nОбновленный POJO с изменённым аргументом:\n")
    # Вызов метода 'toStringMainPojo' класса 'MainPojo'
    Mp.toStringMainPojo()
    # Вызов метода 'toStringTimetable' класса 'Timetable'
    Tt.toStringTimetable()
    # Вызов метода 'toStringSubject' класса 'Subject'
    Su.toStringSubject()
    # Вызов метода 'toStringTeacher' класса 'Teacher'
    Te.toStringTeacher()
    # Вывод в консоль знака '*' 100 раз
    print("*" * 100)

    # Вывод в консоль текста 'Выполненная десериализация - изначальный POJO класс:'
    print("\nВыполненная десериализация - изначальный POJO класс:\n")
    # Открытие файла 'pickle.pickle' для чтения
    with open(output_file, 'rb') as file:
        # Считывание файла 'pickle.pickle'
        (Mp, Tt, Su, Te) = pickle.load(file)

    # Вызов метода 'toStringMainPojo' класса 'MainPojo'
    Mp.toStringMainPojo()
    # Вызов метода 'toStringTimetable' класса 'Timetable'
    Tt.toStringTimetable()
    # Вызов метода 'toStringSubject' класса 'Subject'
    Su.toStringSubject()
    # Вызов метода 'toStringTeacher' класса 'Teacher'
    Te.toStringTeacher()
    # Вывод в консоль знака '*' 100 раз
    print("*" * 100)
 
