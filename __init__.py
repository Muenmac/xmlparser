import xml.etree.ElementTree as ET
from builtins import print

path = '/media/sf_D_DRIVE/Transfer_VM/2019-05-22 Testkunde.xml'
data = '2019-05-22 Testkunde.xml'

tree = ET.parse(path)
root = tree.getroot()

#Find Customer ID in in XML

cust_no = [elem for elem in root.iter("CUSTOMER_ID")]
print(cust_no)

#Change customer ID to None
for foo in root.iter("CUSTOMER_ID"):
    foo_new = None
    foo.text = foo_new
print(foo.text)

#Save new file
tree.write("/media/sf_D_DRIVE/Transfer_VM/2019-05-22 Testkunde_empty.xml")


path_empty = '/media/sf_D_DRIVE/Transfer_VM/2019-05-22 Testkunde_empty.xml'
tree = ET.parse(path_empty)
root = tree.getroot()

print(ET.tostring(root, encoding="utf8").decode('utf8'))




# Print the whole XML as a Text string
#print(ET.tostring(root, encoding='utf8').decode('utf8'))

# Using a list comprehension to iterate over all elements in XML and print all elements
#[print(elem.tag) for elem in root.iter()]

"""
# Doing the same as above with a standard loop
for elem in root.iter():
    print(elem.tag)
"""

#Open file and re-check changes

"""cust_remove = root.find("ORDER_ID")
print(cust_remove)"""

#Print all texts for each element in XML
#[print(elem.text) for elem in root.iter()]

