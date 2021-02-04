#!/usr/bin/python
# -*- coding: latin-1 -*-

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
#username = os.getenv('username')
#pw = os.getenv('pw')



# Test Data
testjob = {
  "title": "Cool Title",
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
def getJobID():
   # wait until server has downloaded files
   time.sleep(300)
   res = requests.get("http://0.0.0.0:8080/api/v1/jobs") 
   
   # Post Test Data to /jobs Endpoint
   #print("\n JSON AN FRONTEND ÜBERGEBEN \n")
   x = requests.post("http://0.0.0.0:8080/api/v1/jobs", json=testjob, headers={"Content-Type": "application/json"})
   print(x)

   # Get Job ID
   print("\n ID DES JOBS ERFRAGEN \n")

   j = requests.get("http://0.0.0.0:8080/api/v1/jobs")
   rjson = j.json()
   job_id = rjson['jobs'][-1]['id']
   print(rjson)
   print(job_id)
   create_json(job_id)

def create_json(job_id):
  data_set = {
  "url": "http://0.0.0.0:8080/api/v1",
  "openapi": "https://raw.githubusercontent.com/Open-EO/openeo-api/1.0.0/openapi.yaml",
  "variables": { },
  "endpoints": {
    "endpoint.default": {
      "url": "/",
      "request_type": "GET",
      "group": "OpenEO API endpoints"
    },
    "endpoint.well-known.openeo": {
      "url": "/.well-known/openeo",
      "request_type": "GET",
      "group": "OpenEO API endpoints"
    },
    "endpoint.collections": {
      "url": "/collections",
      "request_type": "GET",
      "group": "OpenEO API endpoints"
    },
    "endpoint.processes": {
      "url": "/processes",
      "request_type": "GET",
      "group": "OpenEO API endpoints"
    },
    "endpoint.jobs": {
      "url": "/jobs",
      "request_type": "GET",
      "group": "OpenEO API endpoints"
    },
    "endpoint.jobs_post": {
      "url": "/jobs",
      "request_type": "POST",
      "body": "/home/runner/work/TestRepo/TestRepo/testjob_sst.json",
      "group": "OpenEO API endpoints"
    },
    "endpoint.jobs_get": {
      "url": "/jobs/" + job_id,
      "request_type": "GET",
      "group": "OpenEO API endpoints"
    },
    "endpoint.jobs_delete": {
      "url": "/jobs/" + job_id,
      "request_type": "DELETE",
      "group": "OpenEO API endpoints"
    },
    "endpoint.jobs_patch": {
      "url": "/jobs/" + job_id,
      "request_type": "PATCH",
      "body": "/home/runner/work/TestRepo/TestRepo/validator_patch.json",
      "group": "OpenEO API endpoints"
    },
    "endpoint.jobs_results_get": {
      "url": "/jobs/" + job_id + "/results",
      "request_type": "GET",
      "group": "OpenEO API endpoints"
    },
    "endpoint.jobs_results_post": {
      "url": "/jobs/" + job_id + "/results",
      "request_type": "POST",
      "group": "OpenEO API endpoints"
    },
    "endpoint.data": {
      "url": "/data",
      "request_type": "POST",
      "body": "/home/runner/work/TestRepo/TestRepo/testjob_ndvi.json",
      "group": "Own endpoints"
	    
    }
    }
  }
  
  json_dump = json.dumps(data_set)
  print(json_dump)
  with open('validator.json', 'w') as f:
    json.dump(data_set, f)

  print(os.getcwd())
  
getJobID()
  
  
  
  
  
