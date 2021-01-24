import requests
import time
import testjob.json

def getData():
    time.sleep(0.01)
    #requests.get("http://0.0.0.0:8080/api/v1/jobs")
    requests.post("http://0.0.0.0:8080/api/v1/jobs", json=testjob.json, headers={"Content-Type": "application/json"})
    
    
getData()    
