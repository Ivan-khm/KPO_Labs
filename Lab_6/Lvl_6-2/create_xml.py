from xml.dom import minidom


class CreateXml:

    def create_xml(self):
        doc = minidom.Document()

        # Создание основного тега 'Timetable'
        root = doc.createElement('Timetable')
        doc.appendChild(root)

        # Создание тега 'Subject'
        Subject = doc.createElement('Subject')
        # Добавление атрибута 'name_sub' и присвоение ему значения 'KPO'
        Subject.setAttribute('name_sub', 'KPO')
        root.appendChild(Subject)

        # Создание подтега 'Day' в тег 'Subject'
        Day = doc.createElement('Day')
        # Добавление текста 'Saturday' в тег 'Day'
        d = doc.createTextNode('Saturday')
        Day.appendChild(d)
        Subject.appendChild(Day)

        # Создание подтега 'Audience' в тег 'Subject'
        Audience = doc.createElement('Audience')
        # Добавление текста 'D-505' в тег 'Audience'
        a = doc.createTextNode('D-505')
        Audience.appendChild(a)
        Subject.appendChild(Audience)

        # Создание тега 'Teacher'
        Teacher = doc.createElement('Teacher')
        # Добавление атрибута 'full_name' и присвоение ему значения 'Kurganskaya O.V.'
        Teacher.setAttribute('full_name', 'Kurganskaya O.V.')
        root.appendChild(Teacher)

        # Создание подтега 'Sub_teach' в тег 'Teacher'
        Sub_teach = doc.createElement('Sub_teach')
        # Добавление текста 'KPO' в тег 'Sub_teach'
        st = doc.createTextNode('KPO')
        Sub_teach.appendChild(st)
        Teacher.appendChild(Sub_teach)

        # Создание подтега 'Count_sub_per_week' в тег 'Teacher'
        Count_sub_per_week = doc.createElement('Count_sub_per_week')
        # Добавление текста '2' в тег 'Count_sub_per_week'
        cspw = doc.createTextNode('2')
        Count_sub_per_week.appendChild(cspw)
        Teacher.appendChild(Count_sub_per_week)

        # Создание подтега 'Count_students' в тег 'Teacher'
        Count_students = doc.createElement('Count_students')
        # Добавление текста '18' в тег 'Count_students'
        cs = doc.createTextNode('18')
        Count_students.appendChild(cs)
        Teacher.appendChild(Count_students)

        xml_str = doc.toprettyxml(indent="  ")

        # print(xml_str)
        with open("created_xml.xml", "w") as f:
            f.write(xml_str)
