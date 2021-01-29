import json
import os
# https://github.community/t/can-i-access-the-value-in-an-env-file-from-a-python-script-using-os-getenv/139439/2
# https://github.community/t/using-secrets-for-code-and-database-credentials/135875/6
#print(os.environ.items())
print(os.getenv('pw'))

def test():
  json = {'assets': {'8d615358-6144-11eb-ab20-0242ac120006.nc': {'href': 'http://localhost:8080/download/846668b0-6144-11eb-a2b4-0242ac120004/8d615358-6144-11eb-ab20-0242ac120006'}}, 'geometry': None, 'id': '846668b0-6144-11eb-a2b4-0242ac120004', 'links': [], 'properties': {'created': '2021-01-28T08:40:47.19Z', 'datetime': '2021-01-28T08:45:47.29Z', 'description': 'Example Description', 'end_datetime': '2021-01-28T08:41:02.26Z', 'start_datetime': '2021-01-28T08:40:52.18Z', 'title': 'Example Title'}, 'stac_version': '1.0.0', 'type': 'Feature'}
  newjson = json['assets']
  key = list(newjson.items())[0]
  key_new= key[0]

  link_json = {'8d615358-6144-11eb-ab20-0242ac120006.nc': {'href': 'http://localhost:8080/download/846668b0-6144-11eb-a2b4-0242ac120004/8d615358-6144-11eb-ab20-0242ac120006'}}
  link = link_json.get(key_new)
  print(link)
  href = link.pop('href')
  #href = list(link.values())[0]
  print(href)

  return href

#test()


