# TestRepo
_test72
# Testconception

**Todo's:**

 * *Noch R- und JS-Client Tests in der Readme ergänzen*
 * *Testdaten und -größen*
 * *Links hinzufügen*
 
## Test Environment:

**pytest** is used as a testing framework
   
# Test Classes

## Unittests

* The repositories of the Microservices (__submodules__ of this repository) contain test folders with Python-Files, which include Unittests 
   * _These commands can be executed using the command `pytest`_
   * _Unittests are written by the responsible developerteams and are only checked and optimized by the testing team_   


## End-to-end Tests

* End-to-end Tests run with **docker-compose** and test the communication between microservices by executing multiple HTTP-Requests to different endpoints of multiple services
  * _e2e-Tests are written by the testing team and are deployed in the TestRepo in [e2e_ndvi.py](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/e2e_ndvi.py) and [e2e_sst.py](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/e2e_sst.py)  
  
  
  
# OpenEO Backend-Validator

The [OpenEO Backend-Validator](https://github.com/Open-EO/openeo-backend-validator) can be used to assess the __Open-EO conformity__ of our Backend by referring to a prepared [config.json](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/config.json) 



# Github Actions

 * The test methods listed above are integrated in __Continuous Integration__ through Github Actions
 * As a Linting-Tool we use __flake8__ to check for correct Python Syntax
 * The [Unittest-Workflow](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/.github/workflows/Unittest.yml) runs by schedule three times a day, as well as on certain events like pull-requests
   * _The Unittest-Workflow depends on the [Update-Submodules Workflow](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/.github/workflows/Update_submodules.yml), which ensures that all submodules are up to date and the latest requirements can be installed
   * _The Unittest-Workflow also hands back a __coverage report__ regarding the __Testcoverage__ by using the pytest-plugin __pytest-cov__
   * _If the Unittest-Workflow fails, the responsible developer teams receive an email, so that they can fix the problem that occured_
 
 *  In the [Backend-Validator Workflow](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/.github/workflows/backend-validator.yml) the openEO backend validator is installed and  tests for openEO Conformity
   * In the [End to End Workflow](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/.github/workflows/EndToEnd.yml) __End-to-End Tests are executed__
    



# R Client

Eine Anleitung um sich mit dem [openEO R-Client](https://openeo.org/documentation/1.0/r/) mit unserem Backend zu verbinden befindet sich in diesem [Issue](https://github.com/GeoSoftII2020-21/TestRepo/issues/7). Das Ausführen dieses [Skripts](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/R-Client%20Script.R) ermöglicht eine lokale Verbindung zu unserem Backend und beinhaltet eine direkt ausführbare __Test Suite__ . Dafür sollte vorher das Backend über __docker-compose up__ gestartet sein. 

## Testumgebung

Als Testframework für den R-Client wird __testthat__ genutzt




  

