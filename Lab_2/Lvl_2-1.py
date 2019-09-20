from tkinter.filedialog import askopenfilename
import sys


class Class:
    def space(self, text):
        print("\nСлова, удовлетворяющие условию: ")
        for i in range(0, (len(text)-1)):
            word = text[i]  # Текущее слово
            next_word = text[i + 1]  # Следующее слово
            if word.isalpha() and next_word.isalpha():  # Если слова содержат только буквы
                if word[-1].lower() == next_word[0].lower():  # Если последняя буква текущего слова = первой букве
                                                              # следующего слова
                        print(word, ", ", next_word)  # Вывод слов


if __name__ == "__main__":
    try:
        open_file = askopenfilename(filetypes=[('Txt files', '.txt')])  # Выбор текстового файла
        file = open(open_file, 'r')  # Открытие для чтения
        read_file = file.read()  # Считывание файла

        if read_file == "":
            print("\nФайл пуст!")
            sys.exit()
        else:
            read_file.replace("\n", " ")  # Замена символа переноса строки на пробел
            spisok = read_file.split()  # Разделение текста на слова
            file.close()  # Закрытие файла
            print("\n Список слов текста: \n", spisok)
            a = Class()  # Создание объекта класса
            a.space(spisok)  # Вызов функции space

    except FileNotFoundError:
        print("\nФайл не выбран!")
 
