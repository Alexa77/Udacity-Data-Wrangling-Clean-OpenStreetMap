# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:15:30 2015

@author: Dalaska
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json
#import ijson 


#def test():  
    #process_map(OSMFILE)
    #pprint.pprint(result["result"])
with open('vashon.osm.json') as f:
  data = json.loads(f.read())
  #pprint.pprint(data)
key_types={}
for elem in data:
    keys_elem=elem.keys()
    for keys in keys_elem:
        if keys in key_types:
                key_types[keys]=key_types[keys]+1
        else:
                key_types[keys]=1   

import operator
sorted_x = sorted(key_types.items(), key=operator.itemgetter(1))               
#if __name__ == "__main__": 
#    test()
