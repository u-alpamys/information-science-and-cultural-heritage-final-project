from lxml import etree

my_xml = etree.parse("pulp_fiction.xml")
my_xslt = etree.parse("style.xslt")

convert = etree.XSLT(my_xslt)
result = convert(my_xml)

with open("pulp_fiction.html", "wb") as f:
    f.write(etree.tostring(result, pretty_print=True))

print("Conversion is finished")