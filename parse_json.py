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
    data = []
    for _, element in ET.iterparse(file_in):
           #pprint(element)
            el = shape_element(element)
            if el:
                data.append(el)
    return data

def in_query():
    # Write the query
    #query = {"manufacturer":"Ford Motor Company", 
    #         "assembly":{"$in":["Germany", "United Kingdom", "Japan"]}}
    #query = {"amenity":"bank"}
    


    return query

def make_pipeline():
    # complete the aggregation pipeline
    # most common source
    #pipeline = [ #{ "$match" : {"$name" : { "$gt":0 }}},
    #            { "$group" : { "_id" : "$source","count": {"$sum": 1 }}},
    #            { "$sort" : { "count" : -1 }},
                #{ "$skip" : 1 },
                #{ "$limit" : 1 }
    #            ]
    # most common amrity
    pipeline = [ #{ "$match" : {"$name" : { "$gt":0 }}},
                { "$group" : { "_id" : "$amenity","count": {"$sum": 1 }}},
                { "$sort" : { "count" : -1 }},
                { "$skip" : 1 },
    #            { "$limit" : 1 }
               ]
    return pipeline

def aggregate(db, pipeline):
    result = db.vashon.aggregate(pipeline)
    return result
    
def load_data(file_in):
    db = get_db()    
    data = process_map(file_in, True)
    for x in data:
        add_data(db,x)
    return db

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the process_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
    
    db=load_data(OSMFILE)
    print (db.vashon.count())
    #print (db.vashon.find({'type':'way'}).count())
    #print (db.vashon.find({'amenity':'bank'}))
    #print (db.vashon.find({'amenity':'bank'}).count())
    #query = in_query()
    #result=db.vashon.find(query,{"name":1})
    #for a in result:
    #    pprint.pprint(a)
    
    pipeline = make_pipeline()    
    result = aggregate(db, pipeline)
    #print(result)
    pprint.pprint(result["result"])
   
if __name__ == "__main__": 
    test()
    