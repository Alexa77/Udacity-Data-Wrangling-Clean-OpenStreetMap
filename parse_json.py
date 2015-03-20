#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json
 

OSMFILE = "vashon.osm"

def get_db():
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.examples
    return db
    
def add_data(db,d_in):
    # Changes to this function will be reflected in the output. 
    # All other functions are for local use only.
    # Try changing the name of the city to be inserted
    db.vashon.insert(d_in)
    
def process_map(file_in, pretty = False):
    # You do not need to change this file
    data = []
    for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
    return data

def in_query():
    # Write the query
    #query = {"manufacturer":"Ford Motor Company", 
    #         "assembly":{"$in":["Germany", "United Kingdom", "Japan"]}}
    query = {"amenity":"bank"}
    return query

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the process_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
    db = get_db()    
    data = process_map(OSMFILE, True)
    #db.cities.insert(data[1])
    for x in data:
        add_data(db,x)
    #    pprint.pprint(x)
    print (db.vashon.count())
    print (db.vashon.find({'type':'way'}).count())
    print (db.vashon.find({'amenity':'bank'}))
    print (db.vashon.find({'amenity':'bank'}).count())
    query = in_query()
    rt=db.vashon.find({"amenity":"bank"},{"name":1})
    for a in rt:
        pprint.pprint(a)
   
if __name__ == "__main__": 
    test()