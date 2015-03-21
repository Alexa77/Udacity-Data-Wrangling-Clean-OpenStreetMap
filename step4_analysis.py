#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task:
1. to mongo db
2. quary and anayts

"""

import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json

def insert_data(data, db):
    db.vashon3.insert(data)

def load_data(file_in):
    with open(file_in) as f:
        data = json.loads(f.read())
    return data

def get_db():
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.examples
    return db
   
if __name__ == "__main__": 
    # load data
    #data = load_data('vashon_cleaned.json')

    # connect to mongo db
    #db=get_db()
    
    # insert data    
    #insert_data(data, db)
    
    # quarys
    print(db.vashon3.count()) # of data
    print (db.vashon3.find({'type':'way'}).count()) # of way 
    print (db.vashon3.find({'type':'node'}).count()) # of nodes
    print (db.vashon3.find({'amenity':'bank'}).count()) # how many banks
    
    # most common source
    pipeline = [ { "$group" : { "_id" : "$source","count": {"$sum": 1 }}},
                 { "$sort" : { "count" : -1 }},
                 #{ "$skip" : 1 },
                 #{ "$limit" : 1 }
                 ]
    result = db.vashon3.aggregate(pipeline)
    pprint.pprint(result["result"])
    # most common amrity
    #pipeline = [ #{ "$match" : {"$name" : { "$gt":0 }}},
    #            { "$group" : { "_id" : "$amenity","count": {"$sum": 1 }}},
    #            { "$sort" : { "count" : -1 }},
    #            { "$skip" : 1 },
    #            { "$limit" : 1 }
    #           ]
    
    # 

    