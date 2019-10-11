import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.Operator_name = ""
        self.Payroll = ""
        self.Call_prices = ""
        self.Inside = ""
        self.Outside = ""
        self.Stationary = ""
        self.SMS_price = ""
        self.Parameters = ""
        self.Favourite_num = ""
        self.Tarification = ""
        self.Connection_fee = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "Name":
            print("\n**********************")
            name = attributes["name"]
            print("name:", name)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "Operator_name":
            print("Operator_name:", self.Operator_name)
        elif self.CurrentData == "Payroll":
            print("Payroll:", self.Payroll)
        elif self.CurrentData == "Call_prices":
            print("Call_prices:", self.Call_prices)
        elif self.CurrentData == "Inside":
            print("Inside:", self.Inside)
        elif self.CurrentData == "Outside":
            print("Outside:", self.Outside)
        elif self.CurrentData == "Stationary":
            print("Stationary:", self.Stationary)
        elif self.CurrentData == "SMS_price":
            print("SMS_price:", self.SMS_price)
        elif self.CurrentData == "Parameters":
            print("Parameters:", self.Parameters)
        elif self.CurrentData == "Favourite_num":
            print("Favourite_num:", self.Favourite_num)
        elif self.CurrentData == "Tarification":
            print("Tarification:", self.Tarification)
        elif self.CurrentData == "Connection_fee":
            print("Connection_fee:", self.Connection_fee)
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "Operator_name":
            self.Operator_name = content
        elif self.CurrentData == "Payroll":
            self.Payroll = content
        elif self.CurrentData == "Call_prices":
            self.Call_prices = content
        elif self.CurrentData == "Inside":
            self.Inside = content
        elif self.CurrentData == "Outside":
            self.Outside = content
        elif self.CurrentData == "Stationary":
            self.Stationary = content
        elif self.CurrentData == "SMS_price":
            self.SMS_price = content
        elif self.CurrentData == "Parameters":
            self.Parameters = content
        elif self.CurrentData == "Favourite_num":
            self.Favourite_num = content
        elif self.CurrentData == "Tarification":
            self.Tarification = content
        elif self.CurrentData == "Connection_fee":
            self.Connection_fee = content


if __name__ == "__main__":
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("Tarif_mob_comps")
