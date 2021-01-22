import requests
import time

def getData():
    time.sleep(0.01)
    requests.get("http://0.0.0.0:8080/api/v1/jobs")
    
getData()    
