from tkinter.filedialog import askopenfilename
import sys


class Class:
    def find(self, word_pattern, text):  # Метод поиска слова по заданному шаблону
        for word in text:
            if word.lower() == word_pattern.lower:  # Если слова совпадают
                file = open("txt_Lvl_2-4_find.txt", "w")  # Создание файла
                file.write(str(word))  # Запись найденного слова в созданный файл
                file.close()  # Закрытие файла

    def dedicated(self, text):  # Метод определения слов, разделенных пробелами
        for i in range(0, len(text)):  # Цикл до конца текста
            if text[i][0].isalpha() and text[i][0].islower() and text[i][len(text[i])-1].isalpha():  # Если первый и
                                                                                        # последний символ слова - буква
                mas.append(text[i])  # Добавление слова в список слов, разделенных пробелами
        return mas


if __name__ == "__main__":
    try:
        open_file = askopenfilename(filetypes=[('Txt files', '.txt')])  # Выбор текстового файла
        file = open(open_file, 'r')  # Открытие для чтения
        read_file = file.read()  # Считывание файла

        if read_file == "":  # Проверка на пустой файл
            print("\nФайл пуст!")
            sys.exit()  # Завершение программы
        else:
            mas = []
            spisok = read_file.split()  # Разделение текста на слова
            file.close()  # Закрытие файла
            word_p = input("\nВведите солво-шаблон: ")
            print("\n Текст файла: \n", read_file)  # Вывод текста файла
            obj = Class()  # Создание объекта класса
            list_ded = obj.dedicated(spisok)  # Вызод метода dedicated
            print("\nСлова, разделенные пробелами:")
            for i in range(0, len(list_ded)):  # Вывод слов, разделенных пробелами
                print(list_ded[i])
            find_word = obj.find(word_p, read_file)  # Вызов метода find
            print("\nНайденное слово добавлено в текстовый файл: txt_Lvl_2-4_find.txt")

    except FileNotFoundError:
        print("\nФайл не выбран!")
