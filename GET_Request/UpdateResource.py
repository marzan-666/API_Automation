import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

#Read Input Json file
file = open('C:\\Users\\user\\PycharmProjects\\APIautomation\\UpdateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

#Make put request with json input body

response = requests.put(url, request_json)


#Validating response code
assert response.status_code == 200

#Fetch header from response
#print(response.headers.get('Content-Length'))

#Parse Response to json format
response_json = json.loads(response.text)

#Pick ID using JsonPath
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])