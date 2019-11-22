import xml.etree.ElementTree as xml


class Converter:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getXML(self):
        xmls = XML()

        title = self.__builder.getTitle()
        xmls.setTitle(title)

        author = self.__builder.getAuthor()
        xmls.setAuthor(author)

        text = self.__builder.getText()
        xmls.setText(text)

        hashCode = self.__builder.getHashCode()
        xmls.setHashCode(hashCode)

        return xmls


# продукт
class XML:
    def __init__(self):
        self.__title = None
        self.__aut = None
        self.__text = None
        self.__hash = None

    # Тег Title
    def setTitle(self, title):
        self.__title = title

    # Тег Author
    def setAuthor(self, aut):
        self.__aut = aut

    # Тег Text
    def setText(self, text):
        self.__text = text

    # Тег HashCode
    def setHashCode(self, hash):
        self.__hash = hash

    # создание xml файла
    def createXML(self):
        root = xml.Element("Article")
        title = xml.SubElement(root, "Title")
        title.text = self.__title.titl
        author = xml.SubElement(root, "Author")
        author.text = self.__aut.author
        texts = xml.SubElement(root, "Text")
        texts.text = self.__text.symbol
        hashCode = xml.SubElement(root, "HashCode")
        hashCode.text = self.__hash.hashCode
        tree = xml.ElementTree(root)
        # записываем в файл полученный xml
        with open("example.xml", "w"):
            tree.write("example.xml")

        print("\nXML создан!\n")


# строитель
class Builder:
    def getTitle(self): pass

    def getAuthor(self): pass

    def getText(self): pass

    def getHashCode(self): pass


# конкретный строитель
class XMLBuilder(Builder):

    with open("example.txt", "r") as file:
        art = file.read().split("*")

    def getTitle(self):
        title = Title()
        title.titl = self.art[0]
        return title


    def getAuthor(self):
        aut = Author()
        aut.author = self.art[1]
        return aut

    def getText(self):
        text = Text()
        text.symbol = self.art[2]
        return text

    def getHashCode(self):
        hash = HashCode()
        hash.hashCode = self.art[3]
        return hash


# отдельные части:
class Title:
    titl = None


class Author:
    author = None


class Text:
    symbol = None


class HashCode:
    hashCode = None


if __name__ == "__main__":
    xmlBuilder = XMLBuilder()  # initializing the class
    converter = Converter()
    print("Начало работы")
    converter.setBuilder(xmlBuilder)
    res = converter.getXML()
    res.createXML()
    print("Конец работы")
   
