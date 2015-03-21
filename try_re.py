# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:07:28 2015

@author: Dalaska
"""

import re
#print(re.split(r'\s*', 'here are some words'))
#print(re.split(r'(\s*)', 'here are some words'))
#print(re.split(r'(s*)', 'here are some words'))
#print(re.split(r'[a-f]', 'ahldsglakdhgaeogae'))
#print(re.split(r'[a-fA-F0-9]', 'ahldsADGAGglFDGFaDREHkdhgaeogae',re.I|re.M))
#re.I ignore case sensity |re.M evaluate continously
#print(re.split(r'[a-f][a-f]', 'ahldsADGAGglFDGFaDREHkdhgaeogae',re.I|re.M))
#re.I ignore case sensity |re.M evaluate continously
#print(re.split(r'\d','ocinwe324 main st.asdvce'))
#\d digits \Deverything not digit
#print(re.findall(r'\d{1,5}','ocinwe324 main st.asdvce')) #digits range
#print(re.findall(r'\d{1,5}\s\w+\s\w+\.','ocinwe324 main st.dasdvce')) #digits range

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons"]
street_name=re.split(r'\s*', '23 Pie Street SW')
print(re.split(r'\s*', '23 Pie Street SW'))
for x in street_name:
    if x in expected:
        print (x)
        pass
    
#address_regex = re.compile(r'^addr\:')
address_regex = re.compile(r'^addr\:')
comma_ = re.compile(r'\:')

key="addr:street:housenumber"
if address_regex.search(key):
    print('yes')
    key = key.replace('addr:', '') 
    print(key)
    if not comma_.search(key):
        print("yes again")
