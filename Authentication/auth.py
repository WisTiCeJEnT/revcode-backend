from flask import Flask, request, jsonify
from firebase import Firebase

import json

###Set Firebase Configuration###
with open("./Config.json") as json_data:
    config=json.loads(json_data.read())

firebase = Firebase(config)
################################

def signIn():
    data = request.get_json()
    print(data)
    try:
        email = data['email']
        password = data['password']
        user = firebase.auth().sign_in_with_email_and_password(email, password)

        rev = firebase.database().child("users").child(user['localId']).get()
        print('####')
        res = {'email': rev.val()['email'], 'name': str(
            rev.val()['FirstName'])+' '+str(rev.val()['LastName'])}
        print(res)
        return jsonify(res)
    except:
        return "wrong"



def signUp():
    data = request.get_json()
    print(data)
    try:
        email = data['email']
        password = data['password']
        user = firebase.auth().create_user_with_email_and_password(email, password)
        # print('####')
        # print(user)
        res = {user['localId']: {'email': email, 'password': password,
                                 'FirstName': data['first'], 'LastName': data['last']}}
        print(res)
        firebase.database().child("users").update(res)
        return jsonify(user)
    except:
        return "wrong"
