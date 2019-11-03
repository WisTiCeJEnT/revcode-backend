import requests
import json

def poster(url, payload):
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    #print(response.text)
    print(response.json())

def getter(url):
    response = requests.get(url)
    print(response.text)
    print(response)
testjson={
	"name": "กูเองใครจะทำไมวะ",
	"uid": "123456รหัสนี้แหละ"
}
poster("https://revcode.herokuapp.com/adduser",testjson)