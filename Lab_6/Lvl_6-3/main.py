from Create_xml import CreateXml
from UnMarshal import UnMarshal
from Validator import Validator


if __name__ == "__main__":

    # Маршаллизация
    print("Маршаллизация:")
    # Создание объекта класса 'CreateXml'
    cx = CreateXml()
    # Вызов функции 'create_xml' класса 'CreateXml'
    cx.create_xml()
    print("Успешно!\n")

    # Валидация
    print("Валидация:")
    # Создание объекта класса 'Validator'
    val = Validator()
    # Вызов функции 'validate' класса 'Validator'
    # Проверка на соответствие xml документа  и xsd схемы
    if val.validate("created_xml.xml", "xsd_doc.xsd"):
        print('XML file and XSD scheme are valid!\n')
    else:
        print('XML file and XSD scheme are not valid!\n')

    # Демаршаллизация
    print("Демаршаллизация:")
    # Создание объекта класса 'UnMarshal'
    um = UnMarshal()
    # Вызов функции 'unmarshal' класса 'UnMarshal'
    um.unmarshal('created_xml.xml')
 
