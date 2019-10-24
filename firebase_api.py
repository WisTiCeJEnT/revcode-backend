import datetime
import os
import firebase_admin
from firebase_admin import db

def add_new_user(uid, name):
  if(uid not in USER.get().keys()):
      data = {
        "user_data": {
          "uid": uid, 
          "name": name
          },
        "user_storage": {}
      }
      USER.child(uid).update(data)

def get_user_data(uid):
  db_data = USER.child(uid).get()
  res = {}
  res["user_data"] = db_data["user_data"]
  res["user_storage"] = []
  try:
    for item in db_data["user_storage"].keys():
      tmp = {}
      tmp["filename"] = db_data["user_storage"][item]["filename"]
      tmp["extension"] = db_data["user_storage"][item]["extension"]
      tmp["last_edit"] = db_data["user_storage"][item]["date_edit"]
      tmp["file_id"] = item
      res["user_storage"].append(tmp)
    except:
      pass
  return res

def get_file(uid, file_id):
  db_data = USER.child(uid).child("user_storage").child(file_id).get()
  db_data["file_id"] = file_id
  return db_data

def add_new_file(uid):
  data = {
    "code": "",
    "date_create": datetime.datetime.now().strftime("%d-%m-%Y"),
    "date_edit": datetime.datetime.now().strftime("%d-%m-%Y"),
    "extension": "",
    "filename": ""
  }
  firebase_res = USER.child(uid).child("user_storage").push(data)
  return firebase_res.key

def save_file(uid, file_id, file_data):
  data = USER.child(uid).child("user_storage").child(file_id).get()
  data["code"] = file_data["code"]
  data["extension"] = file_data["extension"]
  data["filename"] = file_data["filename"]
  data["date_edit"] = datetime.datetime.now().strftime("%d-%m-%Y")
  USER.child(uid).child("user_storage").child(file_id).update(data)
  return file_id

def remove_file(uid, file_id):
  USER.child(uid).child("user_storage").child(file_id).delete()
  return file_id
  


try:

  cred = firebase_admin.credentials.Certificate("./firebaseServiceAccountKey.json")
  firebase_admin.initialize_app(cred, options={
    'databaseURL': 'https://revcode-83ac0.firebaseio.com',
  })
  USER = db.reference('user')

except:
  print("Get environ key ERROR")
