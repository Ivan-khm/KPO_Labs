from create_xml import CreateXml
from UnMarshal import UnMarshal


if __name__ == "__main__":

    # Маршаллизация
    print("Маршаллизация:")
    # Создание объекта класса 'CreateXml'
    cx = CreateXml()
    # Вызов функции 'create_xml' класса 'CreateXml'
    cx.create_xml()
    print("Успешно!\n")

    # Демаршаллизация
    print("Демаршаллизация:\n")
    # Создание объекта класса 'UnMarshal'
    um = UnMarshal()
    # Вызов функции 'unmarshal' класса 'UnMarshal'
    um.unmarshal('created_xml.xml')
