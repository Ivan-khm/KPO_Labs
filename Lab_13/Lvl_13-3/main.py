from Create_wsdl import Create_wsdl


if __name__ == "__main__":

    # Маршаллизация
    print("Маршаллизация:")
    # Создание объекта класса 'CreateXml'
    cx = Create_wsdl()
    # Вызов функции 'create_xml' класса 'CreateXml'
    cx.create_wsdl()
    print("Успешно!\n")