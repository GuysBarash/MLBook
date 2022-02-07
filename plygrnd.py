import xml.etree.ElementTree as ET
from xml.dom import minidom
from copy import deepcopy

# Open original file
et = ET.parse(r"C:\MLBook\.idea\workspace.xml")

xmlRoot = et.getroot()
for el in list(xmlRoot):
    if el.attrib['name'] != 'RunManager':
        continue

    # Generate new component
    newborn = deepcopy(firstborn)
    firstborn = list(el.getchildren())[0]
    newborn.attrib['name'] = 'BARASH'
    el.append(newborn)
    break

file_name = r"C:\MLBook\.idea\workspacexxxx.xml"
tree = ET.ElementTree(xmlRoot)
tree.write(file_name)
