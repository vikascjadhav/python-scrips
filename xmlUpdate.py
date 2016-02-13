import os
import xml.etree.ElementTree as ET
path = './input'

i = 0 
for fileName in os.listdir(path):
	if not fileName.endswith('.xml'): continue
	fullName = os.path.join(path,fileName)
	tree = ET.parse(fullName)
	root = tree.getroot()
	for node in root.iter('testtag'):
		tmp = str(node.text) + str(i)
		node.text = tmp
	tree.write('output/'+fileName)
