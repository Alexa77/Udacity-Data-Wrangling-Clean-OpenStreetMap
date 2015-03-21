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

DELETE_LIST=['tiger:cfcc','tiger:upload_uuid','tiger:tlid','tiger:reviewed',
             'tiger:name_type','tiger:name_type_1','tiger:name_type_2',
             'gnis:county_id','gnis:created','gnis:feature_id','gnis:state_id',
             'gnis:id','gnis:Cell','gnis:ST_alpha','gnis:County_num','created_by',
             'gnis:edited','source:url','tiger:zip_left_4','is_in:country','source:addr:id','fcc:registration_number'
             'tiger:name_base','tiger:zip_left_3','tiger:zip_left_2','is_in:state_code','tiger:cfcc']
#DELETE_LIST2=['tiger:name_base','tiger:zip_left_3','tiger:zip_left_2','tiger:county','tiger:name_base']
REDUCTENT_LIST=['tiger:name_base','tiger:name_base_1','tiger:name_base_2',
                'tiger:name_direction_prefix','tiger:name_direction_prefix_1','tiger:name_direction_suffix_1',
                'name_1','name_2','name_type',
                'tiger:zip_right_1','tiger:zip_right_2','tiger:zip_right_3','tiger:zip_right_4',
                'tiger:zip_left_1','tiger:zip_right_2''tiger:zip_left_3','tiger:zip_right_4',
                ]
RENAME_LIST=['tiger:source','tiger:county','tiger:zip_left','tiger:zip_right',
             'tiger:separated']
             


def load_data():  
        #process_map(OSMFILE)
        #pprint.pprint(result["result"])
    with open('vashon.osmm.json') as f:
      data = json.loads(f.read())
      #pprint.pprint(data)
def kye_types(data_in): 
    key_types={}
    for elem in data_in:
        keys_elem=elem.keys()
        for keys in keys_elem:
            if keys in key_types:
                    key_types[keys]=key_types[keys]+1
            else:
                    key_types[keys]=1       
    import operator
    sorted_x = sorted(key_types.items(), key=operator.itemgetter(1))
    return sorted_x   
          
def clean_data(data_in):
    data_cleaned = data_in
    for ele in range(0,len(data_cleaned)-1):
        key_list=list(data_cleaned[ele])
        for data_keys in key_list:
            # delete data that dar not usefule
            if data_keys in DELETE_LIST:
                #print(data_keys) #
                data_cleaned[ele].pop(data_keys)
            #if ('name' in key_list) and (data_keys in REDUCTENT_LIST):
            if (data_keys in REDUCTENT_LIST):
                #print(data_keys)
                data_cleaned[ele].pop(data_keys)
            if (data_keys in RENAME_LIST):
                new_name=data_keys.replace('tiger:', '')
                data_cleaned[ele][new_name]=data_cleaned[ele][data_keys]
                data_cleaned[ele].pop(data_keys)
            # rename is in
            if data_keys== 'is_in':
                data_cleaned[ele]['county']=data_cleaned[ele][data_keys]
                data_cleaned[ele].pop(data_keys)
            #if data_keys in DELETE_LIST2:
                #print(data_keys) #
            #    data_cleaned[ele].pop(data_keys)               
    return data_cleaned
    
def save_json(data_in, pretty = False):
    # You do not need to change this file
    file_out = "vashon_cleaned.json"
    data = data_in
    with codecs.open(file_out, "w") as fo:
        fo.write("[")
        for element in data:
            if element:
                if pretty:
                    fo.write(json.dumps(element, indent=2)+","+"\n")
                else:
                    fo.write(json.dumps(element) + ","+ "\n")
        fo.write("]")
    return data
                
##############################
if __name__ == "__main__": 
    #data_cleaned = clean_data(data)
    #key_types = kye_types(data_cleaned)
    #data_cleaned[1].keys()
    # save to jashon
    #save_json(data_cleaned)
    
   
#if 'name' in data_cleaned[1].keys()   :
     


#    test()
#tryit=data_cleaned[1]
#tryit.pop('visible')