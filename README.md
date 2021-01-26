# TestRepo
_test24
# Testkonzeption

**Todo's:**

 * *Noch R- und JS-Client Tests in der Readme ergänzen*
 * *Testdaten und -größen*
 * *Links hinzufügen*
 
## Testumgebung:

als Testframework wird **pytest** verwendet
   
# Testklassen

## Unittests

* In den Repositories der Microservices liegen Testordner mit Python-Files, die Unittests enthalten
   * _Ausführen der Tests über den Befehl `pytest`_
   * _Unittests werden von den Entwicklerteams geschrieben und von den Testern nur geprüft und ergänzt_

## Integrationtests

* Integrationtests laufen über **docker-compose** und testen funktionsübergreifende Funktionalität und die API-Endpunkte
  * _Integrationtests werden von den Testern angelegt und liegen im Testrepository_

## End-to-end Tests

* End-to-end Tests laufen über **docker-compose** und testen die Kommunikation zwischen Microservices und alle HTTP-Methoden der API
  * _e2e-Tests werden von den Testern angelegt und liegen im Testrepository_
  
  
# OpenEO Backend-Validator

Über den Open-EO Backend Validator kann über eine vorgefertigte config-JSON die Open-EO Konformität unseres Backends geprüft werden
[OpenEO Backend-Validator](https://github.com/Open-EO/openeo-backend-validator)

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






  

