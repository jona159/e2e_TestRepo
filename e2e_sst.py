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

def e2e_sst():
   res = requests.get("http://0.0.0.0:8080/api/v1/jobs") 
    
   print("\n JSON AN FRONTEND ÜBERGEBEN \n")
   x = requests.post("http://0.0.0.0:8080/api/v1/jobs", json=testjob, headers={"Content-Type": "application/json"})
   print(x)

   print("\n ID DES JOBS ERFRAGEN \n")

   j = requests.get("http://0.0.0.0:8080/api/v1/jobs")
   rjson = j.json()
   job_id = rjson['jobs'][-1]['id']
   print(rjson)
   print(job_id)

   print("\n DEN JOB AUSFÜHREN ÜBER EINE POST ANFRAGE AN DEN RESULTS ENDPOINT DES JOBS. \n")

   requests.post("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results" , json=None, headers={"Content-Type": "application/json"})

   print("\n WARTEN BIS DER SERVER BEREIT IST \n")
   time.sleep(300)

   print("\n JSON, leer?: \n")
   print(requests.get("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results" ).json())

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
   replacement = re.sub('localhost',  '0.0.0.0', href)
   print(replacement) 
   os.system('wget %s -O netCDF_sst.nc' %replacement)
  
   return replacement
  
e2e_sst()

print("\n CONTENT OF SST NETCDF FILE \n")

fin = xr.open_dataset('netCDF_sst.nc')
print(fin)

print(" \n END OF SST NETCDF FILE \n")

#time.sleep(180)
#stats = os.stat('netCDF_sst.nc')
#print(stats)

