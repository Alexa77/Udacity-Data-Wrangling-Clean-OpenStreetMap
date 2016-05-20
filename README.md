# Clean an area on OpenStreetMap
This project is for the Udacity course on Data Wrangling

## Objective
In this project, the data wrangling process is conducted following a cycle of auditing, cleaning. After the data is cleaned, an analysis is conducted using MongoDB.

## Usage 
### Step1:auditing     
  * Ssource code: “step1_audit. py”     
  * Tasks:      
* audit/count primary tag     
* audit/count secondary tags     
* audit street names     
⋅⋅* I/O: Input original .osm file, no output 

### Step2:parsing
Source code: “step2_parse. py”
Tasks:
* updata street names
* parse the osm file into json
I/O: 
Input original .osm file; 
output parsed json file.

### Step 3: cleaning
Source code:“step3_clean. py”:
Tasks:
* audit and clean secondary tags
I/O: input parsed json file; output cleaned json file

### Step 4: analysis
Source code: “step4_analysis. py”
Tasks:
* import the data into MongoDB
* data analysis using queries in MongoDB
I/O: input cleaned json file, no output


## Software and library requirement:
Python 2.7, pymongo, MongoDB
