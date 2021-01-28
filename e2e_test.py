import json


#example
rjson = {'jobs': [{'created': '2021-01-28T08:40:47.19Z', 'description': 'Example Description', 'id': '846668b0-6144-11eb-a2b4-0242ac120004', 'process': {'process_graph': {'SST': {'arguments': {'bbox': [-999, -999, -999, -999], 'data': {'from_node': 'loadcollection1'}, 'timeframe': ['1981-12-01', '1981-12-17']}, 'process_id': 'mean_sst'}, 'loadcollection1': {'arguments': {'DataType': 'SST', 'timeframe': ['01-12-1981 00:00:00', '30-12-1981 00:00:00', '%d-%m-%Y %H:%M:%S']}, 'process_id': 'load_collection'}, 'save': {'arguments': {'Format': 'netcdf', 'SaveData': {'from_node': 'SST'}}, 'process_id': 'save_result'}}}, 'status': 'created', 'title': 'Example Title'}], 'links': [{'href': 'https://example.openeo.org', 'rel': 'related', 'title': 'openEO', 'type': 'text/html'}]}
job_id = rjson['jobs'][-1]['id']

json = {'assets': {'8d615358-6144-11eb-ab20-0242ac120006.nc': {'href': 'http://localhost:8080/download/846668b0-6144-11eb-a2b4-0242ac120004/8d615358-6144-11eb-ab20-0242ac120006'}}, 'geometry': None, 'id': '846668b0-6144-11eb-a2b4-0242ac120004', 'links': [], 'properties': {'created': '2021-01-28T08:40:47.19Z', 'datetime': '2021-01-28T08:45:47.29Z', 'description': 'Example Description', 'end_datetime': '2021-01-28T08:41:02.26Z', 'start_datetime': '2021-01-28T08:40:52.18Z', 'title': 'Example Title'}, 'stac_version': '1.0.0', 'type': 'Feature'}


link_json = {'0bbe1d06-613d-11eb-b3a4-0242ac120006.nc': {'href': 'http://localhost:8080/download/027b4660-613d-11eb-b581-0242ac120004/0bbe1d06-613d-11eb-b3a4-0242ac120006'}}
link = link_json['href']
print(link)


