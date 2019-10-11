from validator import validate

if validate("Tarif_mob_comps", "Tarid_mob_comps_xsd.xsd"):
    print('XML file and XSD scheme are valid!')
else:
    print('XML file and XSD scheme are not valid!')
