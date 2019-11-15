# Получение пути к файлу и запуск компиллятора
class OriginalProgram:
    FileProgram = ""

    def getFile(self):
        pass

    def setFile(self, PathFile):
        print("Получили файл!\n")


# Читатель
class Reader:

    def readFile(self, FileProgram):
        print("Прочитали текст!\n")

    def startAnalysis(self, BufferProgram):
        pass


# Лексер
class Lexer:
    TableLex = lambda: TableLexems()
    TableId = lambda: TableIdentifier()
    Errors = lambda: Error()

    def lexAnalysis(self):
        print("Получили таблицу лексем, вывели!\n")
        print("Получили таблицу индентификаторов, вывели!\n")


# Синтаксический анализатор (парсер)
class Parser:
    Table = lambda: TableIdentifier()
    Errors = lambda: Error()

    def parsing(self):
        pass


# Семантический анализатор
class SemanticAnalizer:
    Table = lambda: TableIdentifier()
    Errors = lambda: Error()

    def semanticAnalysis(self):
        pass


# Ловит ошибки
class Error:
    ErrorList = ""

    def getErrorList(self):
        pass

    def setErrorList(self, ErrorList):
        pass

    def addError(self, Error):
        pass


# Таблица лексем
class TableLexems:
    LexemList = ""

    def getTable(self):
        pass

    def setTable(self, Table):
        pass

    def addLexem(self, Lexem):
        pass


# Таблица идентификаторов
class TableIdentifier:
    IdentifierList = ""

    def getTable(self):
        pass

    def setTable(self, HashList):
        pass

    def addIdentifier(self, Iden):
        pass


# Подкотовка к генерации
class PrepareGeneration:
    Errors = lambda: Error()

    def createTriads(self):
        pass

    def createDSR(self):
        pass

    def beginGeneration(self):
        pass


# Триады
class Triads:
    TriadsList = ""

    def getList(self):
        pass

    def setList(self):
        print("Получили список триад, вывели!\n")

    def addTriad(self):
        pass


# Дерево синтаксического разбора
class DSR:
    ListDSR = ""

    def getDSR(self):
        pass

    def setDSR(self):
        print("Получили дерево синтаксического разбора, вывели!\n")

    def addDSR(self):
        pass


# Генерация кода
class GenerationCode():
    Triads = lambda: Triads
    DSR = lambda: DSR

    def generate(self):
        print("Получили объектный код, вывели!\n")


if __name__ == '__main__':
    OriginalProgram().setFile(" ")
    Reader().readFile(" ")
    Lexer().lexAnalysis()
    Triads().setList()
    DSR().setDSR()
    GenerationCode().generate()
