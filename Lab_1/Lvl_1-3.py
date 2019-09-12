import sys

class Comparison:
    def compare(self, str):
        sample = "Example"
        if str == sample:
            print("Пароль совпадает с образцом.")
        else:
            print("Пароль не совпадает с образцом")


if __name__ == "__main__":
    string = sys.argv[1]
    a = Comparison()
    a.compare(string)
