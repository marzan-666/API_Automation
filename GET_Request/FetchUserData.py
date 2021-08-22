import requests
import json
import jsonpath

#API URL

url = "https://reqres.in/api/users?page=2"
response = requests.request("GET",url)
print(response)
print(response.content)
print(response.headers)

#Parse response to json format

json_response = json.loads(response.text)
#json.loads(response.decode('utf-8-sig'))

print(json_response)
#print(response.json())


#Fetch value using jsonpath

pages = jsonpath.jsonpath(json_response, 'total_pages')
#print(pages[0])
assert  pages[0] == 4