# from bs4 import BeautifulSoup
# # Reading data from the xml file
# with open('Details.xml', 'r') as f:
#    data = f.read()
#    print(data)
# bs_data = BeautifulSoup(data, 'xml')
# # `bs_data.find_all('Product', {'name':'TV'})`
# for tag in bs_data.find_all('Product', {'name':'TV'}):tag["price"]="Hello!!!"
# # Output the contents of the
# # modified xml file
# print(bs_data.prettify())
# ---------------------------------------------------
import xmltodict
import pprint

# Open the file and read the contents UNICODE TRANSFORMATION FORMAT
with open('Details.xml', 'r') as file:
   my_xml = file.read()

# Use xmltodict to parse and convert
# the XML document
my_dict = xmltodict.parse(my_xml) # xmltodict.parse to convert XML to PYTHONDICT

# Print the dictionary
pprint.pprint(my_dict, indent=4) # Reading complex data in a easier way(pretty print)
