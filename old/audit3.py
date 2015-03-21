"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
#import sys
#sys.modules[__name__].__dict__.clear()
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "vashon.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons","Highway"]

expected2 = ["SE", "SW", "NE", "NW","se","sw","ne","nw"]
# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            'Ave': "Avenue",
            'Rd.': "Road"
            }


def audit_street_type2(street_types, street_name):
    street_words=re.split(r'\s*', street_name)
    regular_name=False
    for word in street_words:       
        if word in expected:
            regular_name=True
    if regular_name==False:
            print(street_name)
            
    for word in street_words:       
        if word in expected2:
            regular_name=True
    if regular_name==False:
            print(street_name)
            
def audit_street_type(street_types, street_name):  
    m = street_type_re.search(street_name)
    if m:
        #print(m)
        #print(m.group())
        street_type = m.group()
        #print(street_type)
        if street_type not in expected:
            #print street_name
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    street_names={}
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type2(street_types, tag.attrib['v'])
                    audit_street_type(street_types, tag.attrib['v'])
                    if elem.tag in street_names.keys():
                              street_names[tag.attrib['v']]=tags[tag.attrib['v']]+1
                    else:
                              street_names[tag.attrib['v']]=1
    return (street_types,street_names)

def count_street_names(osmfile):
        street_names={}
        osm_file = open(osmfile, "r")
        street_types = defaultdict(set)
        for event, elem in ET.iterparse(osm_file, events=("start",)):
            if elem.tag == "node" or elem.tag == "way":
                for tag in elem.iter("tag"):
                    if is_street_name(tag):                          
                          if elem.tag in street_names.keys():
                              street_names[tag.attrib['v']]=tags[tag.attrib['v']]+1
                          else:
                              street_names[tag.attrib['v']]=1               
        return street_names

def update_name(name, mapping):

    # YOUR CODE HERE
    #print (name)
    for x in mapping:
        if name.find(x)>0:
            name=name[0:name.find(x)]+mapping[x]
    return name



def test():
    st_types,street_names = audit(OSMFILE)
    #assert len(st_types) == 3
    pprint.pprint(dict(st_types))
    #streets=count_street_names(OSMFILE)
    pprint.pprint(dict(street_names))
    #for st_type, ways in st_types.iteritems():
    #    for name in ways:
    #        better_name = update_name(name, mapping)
    #        print name, "=>", better_name
    #        if name == "West Lexington St.":
    #            assert better_name == "West Lexington Street"
    #        if name == "Baldwin Rd.":
    #            assert better_name == "Baldwin Road"


if __name__ == '__main__':
    #test()
    st_types,street_names = audit(OSMFILE)
    #assert len(st_types) == 3
    #pprint.pprint(dict(st_types))
    #streets=count_street_names(OSMFILE)
    #pprint.pprint(dict(street_names))
    