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
 

# This function executes a POST HTTP Request to the job endpoint of the frontend microservice
def e2e_ndvi():
   requests.post("http://localhost:80/api/v1/jobs", json=testjob, headers={"Content-Type": "application/json"})
   time.sleep(720)
  
e2e_ndvi()


