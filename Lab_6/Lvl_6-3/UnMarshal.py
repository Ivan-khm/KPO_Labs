import xml.etree.ElementTree as xml


class UnMarshal:

    def unmarshal(self, file):

            # Парсинг xml-файла
            tree = xml.parse(file)
            # Получение основного тега
            main_tag = tree.getroot()
            # Получение остальных тегов
            tag = main_tag.getchildren()

            # Объявление тегов
            name_sub = ''
            Day = ''
            Audience = ''
            full_name = ''
            Sub_teach = ''
            Count_sub_per_week = ''
            Count_students = ''

            # Перебор элементов основного тега
            for i in tag:
                # Если тег = 'Subject'
                if i.tag == "Subject":
                    # Получение аттрибутов тега (словарь)
                    name_sub_dict = i.attrib
                    # Получение значения аттрибута по ключу 'name_sub'
                    name_sub = name_sub_dict.get("name_sub")
                    # Если тег = 'Teacher'
                elif i.tag == "Teacher":
                    # Получение аттрибутов тега (словарь)
                    full_name_dict = i.attrib
                    # Получение значения аттрибута по ключу 'full_name'
                    full_name = full_name_dict.get("full_name")
                # Получение дочернего тега
                element = i.getchildren()

                # Перебор элементов дочерних тегов
                for q in element:
                    # Присвоение переменным значения тегов
                    # Если тег = 'Day'
                    if q.tag == "Day":
                        # Получение текста тега
                        Day = q.text
                    # Если тег = 'Audience'
                    elif q.tag == "Audience":
                        # Получение текста тега
                        Audience = q.text
                    # Если тег = 'Sub_teach'
                    elif q.tag == "Sub_teach":
                        # Получение текста тега
                        Sub_teach = q.text
                    # Если тег = 'Count_sub_per_week'
                    elif q.tag == "Count_sub_per_week":
                        # Получение текста тега
                        Count_sub_per_week = q.text
                    # Если тег = 'Count_students'
                    elif q.tag == "Count_students":
                        # Получение текста тега
                        Count_students = q.text

            # Вывод в консоль полученных данных о предмете
            print("Class Pojo [name_sub = " + name_sub + ", Day = "\
                               + Day + ", Audience = " + Audience + "]")

            # Вывод в консоль полученных данных о преподавателе
            print("Class Pojo [full_name = " + full_name + ", Sub_teach = " + \
                            Sub_teach + ", Count_sub_per_week = " + Count_sub_per_week + \
                            ", Count_students = " + Count_students + "]")
