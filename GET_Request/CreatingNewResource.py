import requests
import json
import  jsonpath

url = "https://reqres.in/api/users"

#Read Input Json file
file = open('C:\\Users\\user\\PycharmProjects\\APIautomation\\CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

#Make post request with json input body

response = requests.post(url, request_json)
print(response.content)

#Validating response code
assert response.status_code == 201

#Fetch header from response
print(response.headers)
print(response.headers.get('Content-Length'))

#Parse Response to json format
response_json = json.loads(response.text)

#Pick ID using JsonPath
id = jsonpath.jsonpath(response_json,'id')
print(id[0])
