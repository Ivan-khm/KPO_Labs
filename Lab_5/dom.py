from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("Tarif_mob_comps")
Tariff = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#    print("Root element : %s" % collection.getAttribute("shelf"))

tariff = Tariff.getElementsByTagName("Name")

for tarrif in tariff:
    print("\n*******************")
    if tarrif.hasAttribute("name"):
        print("Name: %s" % tarrif.getAttribute("name"))

    Operator_name = tarrif.getElementsByTagName('Operator_name')[0]
    print("Operator_name: %s" % Operator_name.childNodes[0].data)
    Payroll = tarrif.getElementsByTagName('Payroll')[0]
    print("Payroll: %s" % Payroll.childNodes[0].data)
    # Call_prices = tarrif.getElementsByTagName('Call_prices')[0]
    # print("Call_prices: %s" % Call_prices.childNodes[0].data)
    Inside = tarrif.getElementsByTagName('Inside')[0]
    print("Inside: %s" % Inside.childNodes[0].data)
    Outside = tarrif.getElementsByTagName('Outside')[0]
    print("Outside: %s" % Outside.childNodes[0].data)
    Stationary = tarrif.getElementsByTagName('Stationary')[0]
    print("Stationary: %s" % Stationary.childNodes[0].data)
    SMS_price = tarrif.getElementsByTagName('SMS_price')[0]
    print("SMS_price: %s" % SMS_price.childNodes[0].data)
    # Parameters = tarrif.getElementsByTagName('Parameters')[0]
    # print("Parameters: %s" % Parameters.childNodes[0].data)
    Favourite_num = tarrif.getElementsByTagName('Favourite_num')[0]
    print("Favourite_num: %s" % Favourite_num.childNodes[0].data)
    Tarification = tarrif.getElementsByTagName('Tarification')[0]
    print("Tarification: %s" % Tarification.childNodes[0].data)
    Connection_fee = tarrif.getElementsByTagName('Connection_fee')[0]
    print("Connection_fee: %s" % Connection_fee.childNodes[0].data)
