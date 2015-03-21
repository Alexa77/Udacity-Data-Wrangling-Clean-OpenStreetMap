#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json
#import ijson 




def test():
   
    #process_map(OSMFILE)
    #pprint.pprint(result["result"])
    with open('vashon.osm2.json') as f:
        data = json.loads(f.read())
    for ele in data: 
        pass
    #pprint.pprint(data)
   
if __name__ == "__main__": 
    test()
    