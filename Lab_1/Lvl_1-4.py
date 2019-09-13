import sys


class Operation:
    def addition(self, count):
        s = int(count[1])
        for i in range(2, len(count)):
            s += int(count[i])
        return s

    def multiply(self, count):
        mult = int(count[1])
        for i in range(2, len(count)):
            mult *= int(count[i])
        return mult


if __name__ == "__main__":
        try:
            count = sys.argv
            obj = Operation()
            s = obj.addition(count)
            m = obj.multiply(count)
            print("\nСумма чисел = ", s)
            print("\nПроизведение чисел = ", m)
        except ValueError:
            print("\nДолжны быть введены целые числа!\n")
 
