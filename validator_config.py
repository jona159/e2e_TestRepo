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

# wait until server has downloaded files
sleep(600)


# Test Data
testjob = {
  "title": "Lame Title",
  "description": "Example Description",
  "process": {
    "process_graph": {
      "loadcollection1": {
        "process_id": "load_collection",
        "arguments": {
          "timeframe" : ["01-06-2020 00:00:00","10-06-2020 00:00:00","%d-%m-%Y %H:%M:%S"],
          "DataType": "Sentinel2",
          "cloudcoverage":[0,30],
          "Login":['username', 'pw']
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

# This function executes a series of HTTP Requests to different microservices of our API to ensure that the communication between them works in a Docker Environment
# It very much mimics the approach from Demo IV: https://github.com/GeoSoftII2020-21/Demos/blob/main/Demo_IV/Demo_IV.ipynb
def getJobID():
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
  "output": "config.json",
  "endpoints": {
    "endpoint1": {
      "url": "/",
      "request_type": "GET"
    },
    "endpoint2": {
      "url": "/.well-known/openeo",
      "request_type": "GET"
	},
	"endpoint3": {
      "url": "/udf_runtimes",
      "request_type": "GET"
	  },
	"endpoint4": {
      "url": "/service_types",
      "request_type": "GET"
    },
    "endpoint5": {
      "url": "/collections",
      "request_type": "GET"
    },
    "endpoint6": {
      "url": "/processes",
      "request_type": "GET"
    },
    "endpoint7": {
      "url": "/jobs",
      "request_type": "GET"
    },
    "endpoint8": {
      "url": "/jobs",
      "request_type": "POST",
      "body": "testjob.json"
	},
    "endpoint9": {
      "url": "/jobs/" + job_id,
      "request_type": "GET"

    }
    }
  }
  
  json_dump = json.dumps(data_set)
  print(json_dump)
  
getJobID()
  
  
  
  
  
