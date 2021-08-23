import requests
import json
import  jsonpath

def add_new_data():
    App_URL = "http://thetestingworldapi.com/Help/Api/POST-api-studentsDetails"
    f = open('C:\\Users\\user\\PycharmProjects\\APIautomation\\Test_End.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(App_URL, request_json)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])
    #print(response.text)

    tech_api_URL = "http://thetestingworldapi.com/Help/Api/POST-api-technicalskills"

    f = open('C:\\Users\\user\\PycharmProjects\\APIautomation\\techDetails.json','r')
    request_json = json.loads(f.read())
    response = requests.post(tech_api_URL, request_json)
    print(response.text)

    add_api_URL = "http://thetestingworldapi.com/Help/Api/PUT-api-addresses-id"

    f = open('C:\\Users\\user\\PycharmProjects\\APIautomation\\address.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(tech_api_URL, request_json)
    print(response.text)

    final_details = "http://thetestingworldapi.com/Help/Api/GET-api-FinalStudentDetails-id/3044"
    response = requests.get(final_details)
    print(response.text)

