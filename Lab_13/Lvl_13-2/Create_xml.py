from xml.dom import minidom


class CreateXml:

    def create_xml(self, mas):
        doc = minidom.Document()

        # Создание основного тега 'Timetable'
        root = doc.createElement('soap:Envelope')
        root.setAttribute('xmlns:soap', 'http://example.schemas.xmlsoap.org/soap/envelope/')
        doc.appendChild(root)

        # Создание тега 'Subject'
        Body = doc.createElement('soap:Body')
        # Добавление атрибута 'name_sub' и присвоение ему значения 'KPO'
        root.appendChild(Body)

        # Создание подтега 'Day' в тег 'Subject'
        productID = doc.createElement(mas[0])
        # Добавление текста 'Saturday' в тег 'Day'
        d = doc.createTextNode('12345')
        productID.appendChild(d)
        Body.appendChild(productID)

        # Создание подтега 'Day' в тег 'Subject'
        Year = doc.createElement(mas[1])
        # Добавление текста 'Saturday' в тег 'Day'
        w = doc.createTextNode('2019')
        Year.appendChild(w)
        Body.appendChild(Year)

        # Создание подтега 'Day' в тег 'Subject'
        Month = doc.createElement(mas[2])
        # Добавление текста 'Saturday' в тег 'Day'
        e = doc.createTextNode('July')
        Month.appendChild(e)
        Body.appendChild(Month)

        xml_str = doc.toprettyxml(indent="  ")

        # print(xml_str)
        with open("created_xml.xml", "w") as f:
            f.write(xml_str)
