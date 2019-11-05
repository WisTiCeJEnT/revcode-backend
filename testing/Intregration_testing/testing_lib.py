import requests
import json
url = "https://revcode.herokuapp.com"
def getFiles(uid):
    files = []
    urllocal = url+'/userdata?uid='+ str(uid)
    response = requests.get(urllocal)
    for i in (response.json()['userData']['user_storage']):
        files.append(i['filename'])
    return files

def addUser(name, uid, email):
    urllocal =url+'/adduser'
    headers = {'content-type': 'application/json'}
    payload = { 'name': str(name),
                'uid': str(uid),
                'email': str(email)
                }
    response = requests.post(urllocal, data=json.dumps(payload), headers=headers)
    return response.json()['status']



def addFile(uid, filename, extension):
    urllocal = url+'/newfile'
    headers = {'content-type': 'application/json'}
    payload = { 'uid': str(uid),
                'filename': str(filename),
                'extension': str(extension)
                }
    response = requests.post(urllocal, data=json.dumps(payload), headers=headers)
    return response.json()['status']


def saveFile(uid, file_id, code, filename, extension):
    urllocal = url+'/savefile'
    headers = {'content-type': 'application/json'}
    payload = { 'uid': str(uid),
                'file_id': str(file_id),
                'code': str(code),
                'filename': str(filename),
                'extension': str(extension)
                }
    response = requests.post(urllocal, data=json.dumps(payload), headers=headers)
    return response.json()['status']

def removeFile(uid, file_id):
    urllocal = url+'/removefile'
    headers = {'content-type': 'application/json'}
    payload = {'uid': str(uid), 'file_id': str(file_id)}
    response = requests.post(urllocal, data=json.dumps(payload), headers=headers)
    return response.json()['status']


def removeUser(uid):
    urllocal = url+'/removeuser'
    headers = {'content-type': 'application/json'}
    payload = {'uid': str(uid)}
    response = requests.post(urllocal, data=json.dumps(payload), headers=headers)
    return response.json()['status']
