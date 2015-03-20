#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
The output should be a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
#import sys
import xml.etree.ElementTree as ET
import pprint


FILENAME = 'vashon.osm' # Vashon, Washington


def count_tags(filename):
        tags={}
        # find the count of tags in the document
        for event, elem in ET.iterparse(filename):            
            if elem.tag in tags.keys():
                tags[elem.tag]=tags[elem.tag]+1
            else:
                tags[elem.tag]=1               
        return tags
      
def count_tag_keys(filename):
        tag_keys={}
        # find the count of keys in tags
        for event, elem in ET.iterparse(filename):            
            if elem.tag == 'tag' and 'k' in elem.attrib:
                #print(elem.get('k'))
                if elem.get('k') in tag_keys.keys():
                    tag_keys[elem.get('k')]=tag_keys[elem.get('k')]+1
                else:
                    tag_keys[elem.get('k')]=1               
        return tag_keys      

def test():
    # find how many different keys in tags 
    tags = count_tags(FILENAME)
    pprint.pprint(tags)
    
    # find how many seconary keys in "tag" 
    tagkeys = count_tag_keys(FILENAME)
    import operator
    sorted_keys = sorted(tagkeys.items(), key=operator.itemgetter(1)) 
    sorted_keys.reverse()
    pprint.pprint(sorted_keys)
    

if __name__ == "__main__":
    test()