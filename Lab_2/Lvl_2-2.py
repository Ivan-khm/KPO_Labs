from tkinter.filedialog import askopenfilename


class Class:
    def edit(self, text):  # Метод изменения слова public на private
        edit_text = text.replace("public", "private")  # Изменение слова public на private
        return edit_text


if __name__ == "__main__":
    try:
        open_file = askopenfilename(filetypes=[('Txt files', '.txt'), ('Java files', '.java')])  # Выбор файла
        file = open(open_file, 'r')  # Открытие для чтения
        read_file = file.read()  # Считывание файла
        file.close()  # Закрытие файла
        obj = Class()  # Создание объекта класса
        edit_file = obj.edit(read_file)   # Вызов метода изменения слов
        file_ed = open(open_file, 'w')  # Открытие файла для записи
        file_ed.write(edit_file)  # Запись измененного текста в файл
        file_ed.close()  # Закрытие файла
        print("\nФайл изменен!")
    except FileNotFoundError:
        print("\nФайл не выбран!")
