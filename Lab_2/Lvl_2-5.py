from tkinter.filedialog import askopenfilename
import sys


class Class:
    def count(self, text):  # Метод подсчета максимального количества подряд идущих цифр в тексте
        c = 0  # Счетчик цифр
        max_c = -1  # Максимальное количество подряд идущих цифр
        for i in range(0, len(text)):  # Цикл от начала до конца текста
            if text[i].isdigit():  # Посимвольная проверка на цифру
                c += 1
            else:
                if max_c < c:
                    max_c = c
                    c = 0
                c = 0
        return max_c


if __name__ == "__main__":
    try:
        open_file = askopenfilename(filetypes=[('Txt files', '.txt')])  # Выбор текстового файла
        file = open(open_file, 'r')  # Открытие для чтения
        read_file = file.read()  # Считывание файла

        if read_file == "":  # Проверка на пустой файл
            print("\nФайл пуст!")
            sys.exit()  # Выход из программы
        else:
            obj = Class()  # Создание объекта класса
            max_k = obj.count(read_file)  # Вызов метода count
            print("\nИсходная строка: ", read_file)  # Вывод исходной строки
            if max_k != 0:
                print("\nМаксимальное количество подряд идущих цифр = ", max_k)
            else:
                print("\nВ тексте нет цифр!")
    except FileNotFoundError:
        print("\nФайл не выбран!")
 
