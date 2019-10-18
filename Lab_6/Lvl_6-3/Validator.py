from lxml import etree


class Validator:

    # Функция проверки на соответствие xml документа  и xsd схемы
    def validate(self, xml_path: str, xsd_path: str) -> bool:
        # Парсер xsd документа
        xmlschema_doc = etree.parse(xsd_path)
        # Создание экземпляра схемы
        xmlschema = etree.XMLSchema(xmlschema_doc)

        # парсер xml документа
        xml_doc = etree.parse(xml_path)
        # Проверка документов xml и xsd
        result = xmlschema.validate(xml_doc)

        # Возврат True (валидация прошла успешно)
        # Возврат False (ошибка валидации)
        return result
