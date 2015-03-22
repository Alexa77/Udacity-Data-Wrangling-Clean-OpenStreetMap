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
    db.tacoma.insert(data)

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
    data = load_data('tacoma_cleaned.json')

    # connect to mongo db
    db=get_db()
    
    # insert data    
    insert_data(data, db)
    
    # quarys
    print('# of data',db.tacoma.count()) # of data
    print ('# of way',db.tacoma.find({'type':'way'}).count()) # of way 
    print ('# of node',db.tacoma.find({'type':'node'}).count()) # of nodes
    print ('# of shools',db.tacoma.find({'amenity':'school'}).count()) # how many banks
    
    
    # number of unqire users
    pipeline = [ { "$group" : { "_id" : "$created.user","count": {"$sum": 1 }}},
                 { "$sort" : { "count" : -1 }},
                 { "$skip" : 1 },
                 ]
    result = db.tacoma.aggregate(pipeline)
    print ('# of users:')    
    print(len(result["result"]))

    # number of unqie users
    pipeline = [ { "$group" : { "_id" : "$created.user","count": {"$sum": 1 }}},
                 { "$sort" : { "count" : -1 }},
                 { "$skip" : 1 },
                 { "$limit" : 5 }
                 ]
    result = db.tacoma.aggregate(pipeline)
    print ('top users:')    
    pprint.pprint(result["result"])
           
    
    # most common source
    pipeline = [ { "$group" : { "_id" : "$source","count": {"$sum": 1 }}},
                 { "$sort" : { "count" : -1 }},
                 { "$skip" : 1 },
                 { "$limit" : 5 }
                 ]
    result = db.tacoma.aggregate(pipeline)
    print ('top 5 source:')    
    pprint.pprint(result["result"])
    
    
    # most common amrity
    pipeline = [ 
                { "$group" : { "_id" : "$amenity","count": {"$sum": 1 }}},
                { "$sort" : { "count" : -1 }},
                { "$skip" : 1 },
                { "$limit" : 5 }
               ]
    result = db.tacoma.aggregate(pipeline)
    print ('top 5 common amrity:')    
    pprint.pprint(result["result"])
    
  
    