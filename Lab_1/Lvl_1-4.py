import sys


class Operation:
    def addition(self, a, b):
        sum = a + b
        return sum

    def multiply(self, a, b):
        mult = a * b
        return mult


if __name__ == "__main__":
        try:
            num_1 = int(sys.argv[1])
            num_2 = int(sys.argv[2])
            obj = Operation()
            s = obj.addition(num_1, num_2)
            print("\nСумма чисел = ", s)
            m = obj.multiply(num_1, num_2)
            print("\nПроизведение чисел = ", m)
        except ValueError:
            print("\nДолжны быть введены целые числа!\n")
        except IndexError:
            print("\nДолжны быть введены два аргумента!\n")
