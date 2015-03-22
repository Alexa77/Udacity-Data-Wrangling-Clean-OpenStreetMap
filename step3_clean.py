# -*- coding: utf-8 -*-
"""
Task:
1.clean street names (already auditted in step 1)
2.audit and clean unnecessary tages 

"""

import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json


DELETE_LIST=['tiger:cfcc','tiger:upload_uuid','tiger:tlid','tiger:reviewed',
             'tiger:name_type','tiger:name_type_1','tiger:name_type_2',
             'name:uk','gnis:county_id','gnis:created','gnis:feature_id','gnis:state_id',
             'gnis:id','gnis:Cell','gnis:ST_alpha','gnis:County_num','created_by',
             'gnis:edited','source:url','tiger:zip_left_4','is_in:country','source:addr:id','fcc:registration_number'
             'tiger:name_base','tiger:zip_left_3','tiger:zip_left_2','is_in:state_code','tiger:cfcc']
REDUCTENT_LIST=['tiger:name_base','tiger:name_base_1','tiger:name_base_2',
                'tiger:name_direction_prefix','tiger:name_direction_prefix_1','tiger:name_direction_suffix_1',
                'name_1','name_2','name_type',
                'tiger:zip_right_1','tiger:zip_right_2','tiger:zip_right_3','tiger:zip_right_4',
                'tiger:zip_left_1','tiger:zip_right_2''tiger:zip_left_3','tiger:zip_right_4',
                ]
RENAME_LIST=['tiger:source','tiger:county','tiger:zip_left','tiger:zip_right',
             'tiger:separated']
             


def load_data():  
    with open('tacoma.json') as f:
      data = json.loads(f.read())
    return data

def clean_street_name(data_in):
    for ele in range(0,len(data_in)-1):
        if 'name' in list(data_in[ele]):
            print(data_in[ele]['name'])
   

def audit_keys(data_in): 
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
                 data_cleaned[ele].pop(data_keys)
            if (data_keys in REDUCTENT_LIST):
                data_cleaned[ele].pop(data_keys)
            if (data_keys in RENAME_LIST):
                new_name=data_keys.replace('tiger:', '')
                data_cleaned[ele][new_name]=data_cleaned[ele][data_keys]
                data_cleaned[ele].pop(data_keys)
            # rename is in
            if data_keys== 'is_in':
                data_cleaned[ele]['county']=data_cleaned[ele][data_keys]
                data_cleaned[ele].pop(data_keys)
                         
    return data_cleaned
    
def save_json(data_in, pretty = False):
    # You do not need to change this file
    file_out = "tacoma_cleaned2.json"
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
                
if __name__ == "__main__": 
    
    # load data    
    #data=load_data()
    
    # audit data
    #key_types = audit_keys(data)
    #print('# of keys: ', len(key_types))

    #clean data
    #data_cleaned = clean_data(data)
    
    # audit cleaned data
    #key_types = audit_keys(data_cleaned)
    #print('# of keys: ',len(key_types))
    
    #save to jashon
    save_json(data_cleaned)
    
