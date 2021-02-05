#@author Judith Becka, https://github.com/a2beckj
#@author Jonas Raabe, https://github.com/jona159

import requests
import json
import time
import sys
import re
import urllib.request
import os
import xarray as xr
import netCDF4
import scipy.io.netcdf
import pytest
#import testjob.json

# Test Data
testjob = {
  "title": "Example Title",
  "description": "Example Description",
  "process": {
    "process_graph": {
      "loadcollection1": {
        "process_id": "load_collection",
        "arguments": {
          "timeframe" : ["01-12-1981 00:00:00","30-12-1981 00:00:00","%d-%m-%Y %H:%M:%S"],
          "DataType": "SST"
        }
        },
        "SST": {
        "process_id": "mean_sst",
        "arguments": {
          "data":{
              "from_node": "loadcollection1"
          },
          "timeframe":["1981-12-01","1981-12-17"],
          "bbox":[-999,-999,-999,-999]
          }
        },
        "save":{
            "process_id": "save_result",
            "arguments":{
                "SaveData":{
                    "from_node":"SST"
                },
                "Format": "netcdf"
            }
        }
      }
      }
    }  

# This function executes a series of HTTP Requests to different microservices of our API to ensure that the communication between them works in a Docker Environment
# It very much mimics the approach from Demo IV: https://github.com/GeoSoftII2020-21/Demos/blob/main/Demo_IV/Demo_IV.ipynb
def e2e_sst():
   res = requests.get("http://0.0.0.0:8080/api/v1/jobs") 
   
   # Post Test Data to /jobs Endpoint
   print("\n JSON AN FRONTEND ÜBERGEBEN \n")
   x = requests.post("http://0.0.0.0:8080/api/v1/jobs", json=testjob, headers={"Content-Type": "application/json"})
   print(x)

   # Get Job ID
   print("\n ID DES JOBS ERFRAGEN \n")

   j = requests.get("http://0.0.0.0:8080/api/v1/jobs")
   rjson = j.json()
   job_id = rjson['jobs'][-1]['id']
   print(rjson)
   print(job_id)

   # Execute Job with a Post Request to jobs/<job_id>/results Endpoint 
   print("\n DEN JOB AUSFÜHREN ÜBER EINE POST ANFRAGE AN DEN RESULTS ENDPOINT DES JOBS. \n")

   requests.post("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results" , json=None, headers={"Content-Type": "application/json"})

   # Wait 5 minutes until Server is ready
   print("\n WARTEN BIS DER SERVER BEREIT IST \n")
   time.sleep(300)
 
   print("\n JSON, leer?: \n")
   print(requests.get("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results" ).json())

   # Get Downloadlink 
   print("\n Downloadlink: \n")
   json = requests.get("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results" ).json()
   newjson = json["assets"]
   print(newjson)
   key = list(newjson.items())[0]
   key_new= key[0]
   
   link = newjson.get(key_new)
   print(link)
   href = link.pop('href')
   print(href)
   # rename localhost to 0.0.0.0 
   replacement = re.sub('localhost',  '0.0.0.0', href)
   print(replacement)
   # start download of netCDF file
   os.system('wget %s -O netCDF_sst.nc' %replacement)
  
   return replacement
  
e2e_sst()

print("\n CONTENT OF SST NETCDF FILE \n")

# Open the Xarray Dataset in the netcdf file, which is stored in our repository for the duration of the action
fin = xr.open_dataset('netCDF_sst.nc')
print(fin)

#print("\n DIMENSIONS \n")

#sst_values = fin['sst'][0]
#print(sst_values)

#print(" \n EMPTY LINE \n ")

#print(fin['sst'][:])

print(" \n END OF SST NETCDF FILE \n")

# Test to assert that the xarray Dataset contains the correct number of values
def test_length_fin():
  assert fin.count() == 1036800

#time.sleep(180)
#stats = os.stat('netCDF_sst.nc')
#print(stats)
