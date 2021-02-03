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

# Login Credentials for Copernicus Scihub
username = os.getenv('username')
pw = os.getenv('pw')


# Test Data
testjob = {
  "title": "Example Title",
  "description": "Example Description",
  "process": {
    "process_graph": {
      "loadcollection1": {
        "process_id": "load_collection",
        "arguments": {
          "timeframe" : ["01-06-2020 00:00:00","10-06-2020 00:00:00","%d-%m-%Y %H:%M:%S"],
          "DataType": "Sentinel2",
          "cloudcoverage":[0,30],
          "Login":[username, pw]
        }
        },
        "ndvi": {
        "process_id": "ndvi",
        "arguments": {
          "data":{
              "from_node": "loadcollection1"
          }
        }
        },
        "save":{
            "process_id": "save_result",
            "arguments":{
                "SaveData":{
                    "from_node":"ndvi"
                },
                "Format": "netcdf"
            }
        }
      }
      }
    }  


def e2e_ndvi():
   res = requests.get("http://0.0.0.0:8080/api/v1/jobs") 
   
   # Post Test Data to /Jobs Endpoint
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

   # Execute Job with a POST Request to /jobs/<job_id>/results Endpoint 
   print("\n DEN JOB AUSFÜHREN ÜBER EINE POST ANFRAGE AN DEN RESULTS ENDPOINT DES JOBS. \n")

   requests.post("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results" , json=None, headers={"Content-Type": "application/json"})

   # Wait 5 minutes until server is ready
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
   os.system('wget %s -O netcdf_ndvi.nc' %replacement)
   
   

   return replacement
  
e2e_ndvi()

print("\n CONTENT OF NDVI NETCDF FILE \n")

# Open the Xarray Dataset in the netcdf file, which is stored in our repository for the duration of the action
fin = xr.open_dataset('netcdf_ndvi.nc')
print(fin)

print(fin['__xarray_dataarray_variable__'][:])

print(" \n END OF NDVI NETCDF FILE \n")

# Test to assert that the xarray Dataset contains the correct number of values
def test_count_fin():
  assert fin.count() == 2303604
