import random


class Document(object):
    def show(self):
        raise NotImplementedError()


# Фигура О
class Figure_O(Document):
    def show(self):
        print(figures[0])


# Фигура I
class Figure_I(Document):
    def show(self):
        print(figures[1])


# фигура S
class Figure_S(Document):
    def show(self):
        print(figures[2])


# фигура Z
class Figure_Z(Document):
    def show(self):
        print(figures[3])


# фигура L
class Figure_L(Document):
    def show(self):
        print(figures[4])


# фигура J
class Figure_J(Document):
    def show(self):
        print(figures[5])


# фигура T
class Figure_T(Document):
    def show(self):
        print(figures[6])


# суперфигура
class Super_figure(Document):
    def show(self):
        print(figures[7])


class Application(object):
    def create_document(self, type_):
        raise NotImplementedError()


class MyApplication(Application):
    # переопределение метода create_document
    def create_document(self, type_):
        # Если индекс = 0
        if type_ == 0:
            return Figure_O()
        elif type_ == 1:
            return Figure_I()
        elif type_ == 2:
            return Figure_S()
        elif type_ == 3:
            return Figure_Z()
        elif type_ == 4:
            return Figure_L()
        elif type_ == 5:
            return Figure_J()
        elif type_ == 6:
            return Figure_T()
        elif type_ == 7:
            return Super_figure()


# список имен фигур
figures = ["O", "I", "S", "Z", "L", "J", "T", "Super figure"]
app = MyApplication()

# переменная для счетчика фигур
c = 1
# цикл до 10 фигур по индексу
for j in range(10):
    # каждая 4 фигура - суперфигура
    if not (c % 4 == 0):
        a = random.randint(0, 6)
        app.create_document(a).show()
    else:
        a = 7
        app.create_document(a).show()
    c += 1
