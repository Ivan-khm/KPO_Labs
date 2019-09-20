from tkinter.filedialog import askopenfilename
import sys


class Class:
    def transpose(self, matrix):  # Метод транспонирования матрицы
        tr_matrix = []
        for j in range(0, len(matrix[0])-1):
            mas = []
            for i in range(0, len(matrix)):
                mas += matrix[i][j]
            tr_matrix += mas
        return tr_matrix


if __name__ == "__main__":
    open_file = askopenfilename(filetypes=[('Txt files', '.txt')])  # Выбор текстового файла
    file = open(open_file, 'r')  # Открытие для чтения
    read_lines = file.readlines()  # Чтение файла
    file.close()
    matrix = ""
    size = len(read_lines[0])-1  # Размер квадратной матрицы

    print("\nПолученная матрица:")  # Вывод исходной матрицы
    for i in range(0, len(read_lines)):
        if read_lines[i].isdigit:  # Проверка на числа(Матрица должна содержать только числа)
            for j in range(0, len(read_lines[i])):
                if read_lines[i][j] != "\\":
                    matrix += read_lines[i][j] + " "
                else:
                    matrix += "\n"
                    break
        else:
            print("Матрица должна содержать только числа")
            sys.exit()

    print("", matrix)
    print("Размер матрицы %s на %s" % (size, size))  # Вывод размера матрицы
    obj = Class()  # Создание объекта класса
    tr_matrix = obj.transpose(read_lines)  # Вызов метода транспонирования матрицы
    trans_m = ""

    print("\nТранспонированная матрица: ")  # Вывод транспонированной матрицы
    q = 0
    for i in range(0, len(tr_matrix)):
        trans_m += tr_matrix[i] + " "
        q += 1
        if q == len(read_lines[0]) - 1:
            trans_m += "\n"
            q = 0
    print(trans_m)
 
