"""
Task:
1.updata street names
2.parse the osm file into json 

The output are a list of dictionaries that look like this:

{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {
          "version":"2",
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",
          "user":"linuxUser16",
          "uid":"1219059"
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"
        },
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}
"""

import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
address_ = re.compile(r'^addr\:')
colom_ = re.compile(r'\:')


CREATED = [ "version", "changeset", "timestamp", "user", "uid"]
POSITION = ['lat', 'lon'] # GPS positon

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            'Ave': "Avenue",
            'Rd.': "Road",
            'SW ': "Southwest ",
            'SE ': "Southeast ",
            'NW ': "Northwest ",
            'NE ': "Northeast "
            
            }
            
def shape_element(element):
    node = {}
    address = {}
    if element.tag == "node" or element.tag == "way":
        
        # add 'type' 
        node['type'] = element.tag 
        
        # add 'created' and others
        for attrbt in element.attrib:
            
            if attrbt in CREATED:
                if 'created' not in node:
                    node['created'] = {}
                node['created'][attrbt] = element.attrib[attrbt]           
            elif attrbt in POSITION:
                continue
            else:
                node[attrbt] = element.attrib[attrbt]
        
        # add pos[lon lat]
        if 'lat' in element.attrib and 'lon' in element.attrib:
            node['pos'] = [float(element.get('lat')), float(element.get('lon'))]
        
        # add secondary tag
        for tag_2nd in element:
            
            # add 'node_refs'
            if tag_2nd.tag == 'nd':
                if 'node_refs' not in node:
                    node['node_refs'] = []
                if 'ref' in tag_2nd.attrib:
                    node['node_refs'].append(tag_2nd.get('ref'))
            
            # ensure the tag, key and value valid       
            if tag_2nd.tag != 'tag' or 'k' not in tag_2nd.attrib or 'v' not in tag_2nd.attrib:       
                continue   # jump off elements not in tag
            key = tag_2nd.get('k')
            val = tag_2nd.get('v')
            if problemchars.search(key):
                continue  # jump off elements with problmetic in keys
            elif address_.search(key):
                key = key.replace('addr:', '') # replace name
                if not colom_.search(key): #search again no second":'
                    address[key] = val
            else:
                node[key] = val
        
        # if address exist        
        if len(address) > 0:
            node['address'] = address
            # updata street name
            if 'street' in node['address']:
                node['address']['street']=update_name(node['address']['street'], mapping)
                #print(node['address']['street'])                
        return node
    else:
        return None

def update_name(name, mapping):
    for x in mapping:
        if name.find(x)>0:
            name=name[0:name.find(x)]+mapping[x]
    return name

def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+","+"\n") # added a comma
                else:
                    fo.write(json.dumps(el) +","+ "\n")
    return data
   
if __name__ == "__main__":
    data = process_map('vashon.osm', True)