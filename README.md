# TestRepo


# Testconception

The listed tests, except for JS- and R-Client, have only been developed by using github actions. 
A local execution of single test classes only took place on a limited scale, so just the correct execution of tests via the github actions can be guaranteed.
Although there should not be a general problem, when trying to set up these test scenarios locally with the given data in this repository or with dynamically generated data within the actions. For setting up JS- and R-Client testscenarios locally, follow instructions below..

## Test Environment:

**pytest** is used as a testing framework

## Test data:

* Testdata for the **unittests** is provided by the development teams that wrote the tests
* Testdata for the **end-to-end tests** is located within the python scripts for checking [SST](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/e2e_sst.py) and [NDVI/SENTINEL](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/e2e_ndvi.py) processes.
* Testdata for the **backend-validator** is located in the [BackendValidator directory](https://github.com/GeoSoftII2020-21/TestRepo/tree/main/BackendValidator) in this repository in json-format.
   
# Test Classes

## Unittests

* The repositories of the Microservices (__submodules__ of this repository) contain test folders with Python-Files, which include Unittests 
   * _These commands can be executed using the command `pytest`_
   * _Unittests are written by the responsible developerteams and are only checked and optimized by the testing team_   


## End-to-end tests

* End-to-end Tests run with **docker-compose** and test the communication between microservices by executing multiple HTTP-Requests to different endpoints of multiple services
  * _e2e-Tests are written by the testing team and are deployed in the TestRepo in [e2e_ndvi.py](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/e2e_ndvi.py) and [e2e_sst.py](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/e2e_sst.py)_  
  * Downloaded files, for both NDVI and SST cases, are copied from the database containers subdirectories to the actions running machine. Then, two test files, [xr_ndvi](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/xr_ndvi.py) and [xr_sst](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/xr_sst.py), are executed, that check  the downloaded files for correctness.
  
  
  
## OpenEO Backend-Validator

The [OpenEO Backend-Validator](https://github.com/Open-EO/openeo-backend-validator) can be used to assess the __Open-EO conformity__ of our Backend by referring to a dynamically by the action created config.json.


## JS- and R-Client tests
In order to check, if the backend is able to communicate with JS- and R-environments, the [openEO JS-Client](https://openeo.org/documentation/1.0/javascript/) and the [openEO R-Client](https://openeo.org/documentation/1.0/r/) have been developed. These have been included into our test-environment.


# Github Actions

 * The test methods listed above are integrated in __Continuous Integration__ through Github Actions
 * As a Linting-Tool we use __flake8__ to check for correct Python Syntax
 * The [Unittest-Workflow](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/.github/workflows/Unittest.yml) runs by schedule three times a day, as well as on certain events like pull-requests
   * _The Unittest-Workflow depends on the [Update-Submodules Workflow](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/.github/workflows/Update_submodules.yml), which ensures that all submodules are up to date and the latest requirements can be installed_
   * _The Unittest-Workflow also hands back a __coverage report__ regarding the __Testcoverage__ by using the pytest-plugin **pytest-cov**_
   * _If the Unittest-Workflow fails, the responsible development teams receive an email, so that they can fix the problem that occured_
 
 * In the [End to End Workflow](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/.github/workflows/EndToEnd.yml) __End-to-End Tests are executed__
    * _In addition to the end to end tests that cover the final implementation, we also provided end to end tests based on the implementation of demo 5_
    
 *  In the [Backend-Validator Workflow](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/.github/workflows/backend-validator.yml) the openEO backend validator is installed and tests for openEO Conformity by schedule three times a day as well
    * _If the Backend-Validator workflow fails, the responsible developer teams receive an email, so that they can fix the problem that occured_
    
    
 * In the [R-Client Workflow](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/.github/workflows/r-client.yml) a connection to our backend is established using the openEO R-Client. Additionally a _test suite_ is executed. 
 
 * In the [JS-Client Workflow](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/.github/workflows/js-client.yml) a connection to our backend is established using the [openEO JS-Client](https://openeo.org/documentation/1.0/javascript/). A [js-script](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/.github/actions/index.js) checks for the correct number of collections and processes provided by the backend.

    



# R Client

* In order to connect to our Backend with the [openEO R-Client](https://openeo.org/documentation/1.0/r/) locally, please follow these Instructions: 
  1. Execute the command `git clone https://github.com/GeoSoftII2020-21/TestRepo`
  2. Execute the command `docker-compose up`
  3. In __RStudio__ or __RConsole__ execute this [Skript](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/R-Client%20Script.R), which also contains a __Test Suite__ 


# JS Client

* In order to connect to our Backend with the [openEO JS-Client](https://openeo.org/documentation/1.0/javascript/) locally, please follow these Instructions: 
  1. Execute the command `git clone https://github.com/GeoSoftII2020-21/TestRepo`
  2. Execute the command `docker-compose up`
  3. Navigate into the js-client folder
  4. Open the html file. After 5 seconds you will be able to see the evaluated test results.

## Test environment

* For the R-Client __testthat__ is used as a testing framework
* For the JS-Client __QUnit__ is used as a testing framework




  

