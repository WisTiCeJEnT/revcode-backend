def getFiles(uid):
    files = []
    url = 'https://revcode.herokuapp.com/userdata?uid='+ str(uid)
    response = requests.get(url)
    for i in (response.json()['userData']['user_storage']):
        files.append(i['filename'])
    return files


def addUser(name, uid):
    url = 'https://revcode.herokuapp.com/adduser'
    headers = {'content-type': 'application/json'}
    payload = { 'name': str(name),
                'uid': str(uid)
                }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()['status']

def addFile(uid, filename, extension):
    url = 'https://revcode.herokuapp.com/newfile'
    headers = {'content-type': 'application/json'}
    payload = { 'uid': str(uid),
                'filename': str(filename),
                'extension': str(extension)
                }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()['status']

def removeFile(uid, file_id):
    url = 'https://revcode.herokuapp.com/removefile'
    headers = {'content-type': 'application/json'}
    payload = {'uid': str(uid), 'file_id': str(file_id)}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()['status']

def removeUser(uid):
    url = 'https://revcode.herokuapp.com/removeuser'
    headers = {'content-type': 'application/json'}
    payload = {'uid': str(uid)}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()['status']

