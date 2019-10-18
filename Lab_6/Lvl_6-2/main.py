from create_xml import CreateXml
from UnMarshal import UnMarshal


if __name__ == "__main__":

    # Маршаллизация
    cx = CreateXml()
    cx.create_xml()

    # Демаршаллизация
    print("Демаршаллизация:\n")
    um = UnMarshal()
    um.unmarshal('created_xml.xml')
