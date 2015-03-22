"""
Task:
1.audit/count tag
2.audit/count secondary tag
3.audit street names

note: no change of data will in this step, they will be made in step 3

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
            "Trail", "Parkway", "Commons", "Highway"] #   added highway

expected2 = ["SE", "SW", "NE", "NW","se","sw","ne","nw"]

def count_tags(filename):
        tags={}
        # find the count of tags in the document
        for event, elem in ET.iterparse(filename):            
            if elem.tag in tags.keys():
                tags[elem.tag]=tags[elem.tag]+1
            else:
                tags[elem.tag]=1               
        return tags
      
def count_secondary_tag(filename):
        tag_keys={}
        # find the count of keys in tags
        for event, elem in ET.iterparse(filename):            
            if elem.tag == 'tag' and 'k' in elem.attrib:
                if elem.get('k') in tag_keys.keys():
                    tag_keys[elem.get('k')]=tag_keys[elem.get('k')]+1
                else:
                    tag_keys[elem.get('k')]=1  
        # sort the tag in reverse order
        import operator
        sorted_keys = sorted(tag_keys.items(), key=operator.itemgetter(1)) 
        sorted_keys.reverse()    
        return sorted_keys      
     
     
def audit_street_type(street_types, street_name):  
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
            
def audit_street_type2(street_types, street_name):    
    # this function is to detect the street names that have the word "street","avenue"
    # in the middle of the street name such as '31st Avenue Southwest'
    #print('irregular street names')    
    street_words=re.split(r'\s*', street_name) # split the into words
    regular_name=False # inicialize
    for word in street_words:       
        if word in expected: # check if any of the words are in the expected value
            regular_name=True
    if regular_name==False:
            print(street_name) 
     
    # check if the street name have abbreiation for direction such as "southwest"        
    regular_name=True # inicialize    
    for word in street_words:
        if word in expected2:
            regular_name=False
    if regular_name==False:
            print(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit_street_name(osmfile):
    street_names={}
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                   audit_street_type(street_types, tag.attrib['v'])
    return street_types

def audit_street_name2(osmfile):
    street_names={}
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                   audit_street_type2(street_types, tag.attrib['v'])



if __name__ == '__main__':
    
    # audit/count tag
    tags = count_tags(OSMFILE)
    print("counts of primary tags:")
    pprint.pprint(tags)
    
    # audit/count secondary tag
    secondary_tag = count_secondary_tag(OSMFILE)
    print("counts of secondary tags:")
    pprint.pprint(secondary_tag)
    
    # audit street names
    print("irregular street names:")
    street_types = audit_street_name(OSMFILE)
    pprint.pprint(dict(street_types))
    
    # audit street names
    print("irregular street names (modified):")
    street_types = audit_street_name2(OSMFILE)

    