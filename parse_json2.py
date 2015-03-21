#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json
#import ijson 

def insert_data(data, db):
# Your code here. Insert the data into a collection 'arachnid'
    db.vashon2.insert(data)




def test():
   
    #process_map(OSMFILE)
    #pprint.pprint(result["result"])
    with open('vashon.osm2.json') as f:
        data = json.loads(f.read())
    #for ele in data: 
    #    pass
    #pprint.pprint(data)
   
if __name__ == "__main__": 
    #test()

   from pymongo import MongoClient
   client = MongoClient('localhost:27017')
   db = client.examples
   with open('vashon.osm2.json') as f:
        data = json.loads(f.read())
   insert_data(data, db)
   print(db.vashon2.find_one())
   print (db.vashon2.find({'type':'way'}).count())