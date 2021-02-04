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

* End-to-end Tests run with **docker-compose** and test the communication between microservices by executing multiple HTTP-Request to different endpoints of multiple services
  * _e2e-Tests are written by the testing team and are deployed in the TestRepo in [e2e_ndvi.py](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/e2e_ndvi.py) and [e2e_sst.py](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/e2e_sst.py)  
  
  
  
# OpenEO Backend-Validator

The [OpenEO Backend-Validator](https://github.com/Open-EO/openeo-backend-validator) can be used to assess the __Open-EO conformity__ of our Backend by referring to a prepared [config.json](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/config.json) 



# Github Actions

 * Über Github Actions werden die oben aufgeführten Testmethoden automatisiert und über einen festen Zeitplan um 6, 12 und 20 Uhr (UTC) jeden Tag ausgeführt
 * Zusätzlich laufen sämtliche Tests auch bei bestimmten Events wie beispielsweise Pull-Requests.
 * In den Github Actions passiert konkret Folgendes: 
   * Submodules werden bei Bedarf geupdatet
   * Requirements werden installiert
   * Über das Linting-Tool flake8 wird der Code auf korrekte Python Syntax überprüft
   * Der Open EO-Backend Validator wird installiert und testet das Backend auf Open EO Konformität
   * Über Docker-compose werden die Container mit den Microservices gestartet sodass Letztere untereinander kommunizieren und e2e Tests ausgefürt werden können
   * Über Pytest werden Unit- und Integrationtests ausgeführt und ein Coverage-Report zurückgegeben 



# R Client

Eine Anleitung um sich mit dem [openEO R-Client](https://openeo.org/documentation/1.0/r/) mit unserem Backend zu verbinden befindet sich in diesem [Issue](https://github.com/GeoSoftII2020-21/TestRepo/issues/7). Das Ausführen dieses [Skripts](https://github.com/GeoSoftII2020-21/TestRepo/blob/main/R-Client%20Script.R) ermöglicht eine lokale Verbindung zu unserem Backend und beinhaltet eine direkt ausführbare __Test Suite__ . Dafür sollte vorher das Backend über __docker-compose up__ gestartet sein. 

## Testumgebung

Als Testframework für den R-Client wird __testthat__ genutzt




  

