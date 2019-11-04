import datetime
import os
import firebase_admin
from firebase_admin import db, auth

def add_new_user(uid, name, email):
  if(uid not in USER.get().keys()):
      data = {
        "user_data": {
          "uid": uid, 
          "name": name,
          "email": email
          },
        "user_storage": {}
      }
      USER.child(uid).update(data)

def get_user_data(uid):
  db_data = USER.child(uid).child("user_data").get()
  db_storage = USER.child(uid).child("user_storage").order_by_child("date_edit").get()
  res = {}
  res["user_data"] = db_data
  res["user_storage"] = []
  for item in db_storage.keys():
    tmp = {}
    tmp["filename"] = db_storage[item]["filename"]
    tmp["extension"] = db_storage[item]["extension"]
    tmp["last_edit"] = cut_date(db_storage[item]["date_edit"])
    tmp["file_id"] = item
    res["user_storage"].append(tmp)
  res["user_storage"] = res["user_storage"][::-1]
  return res

def cut_date(date_string):
  try:
    date = date_string.split("-")
    date_string = f"{date[2]}-{date[1]}-{date[0]}"
  except:
    pass
  return date_string

def get_file(uid, file_id):
  db_data = USER.child(uid).child("user_storage").child(file_id).get()
  db_data["file_id"] = file_id
  db_data["date_edit"] = cut_date(db_data["date_edit"])
  return db_data

def get_indent(uid, file_id, line_no):
  indent = USER.child(uid).child("user_storage").child(file_id).child("indent").get()
  return indent[int(line_no)]

def set_indent(uid, file_id, line_no, new_indent, code):
  file_data = USER.child(uid).child("user_storage").child(file_id).get()
  file_data["indent"].insert(int(line_no)+1, int(new_indent))
  file_data["code"].insert(int(line_no), code)
  USER.child(uid).child("user_storage").child(file_id).update(file_data)

def add_new_file(data):
  uid = data["uid"]
  data = {
    "code": {"0": ""},
    "indent": [0],
    "date_create": datetime.datetime.now().strftime("%d-%m-%Y"),
    "date_edit": datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
    "extension": data["extension"],
    "filename": data["filename"]
  }
  firebase_res = USER.child(uid).child("user_storage").push(data)
  return firebase_res.key

def save_file(uid, file_id, file_data):
  data = USER.child(uid).child("user_storage").child(file_id).get()
  data["code"] = file_data["code"]
  data["extension"] = file_data["extension"]
  data["filename"] = file_data["filename"]
  data["date_edit"] = datetime.datetime.now().strftime("%Y-%m-%d")
  USER.child(uid).child("user_storage").child(file_id).update(data)
  return file_id

def remove_file(uid, file_id):
  USER.child(uid).child("user_storage").child(file_id).delete()
  return file_id

def remove_user(uid):
  USER.child(uid).delete()
  try:
    auth.delete_user(uid)
  except:
    print("Can't delete user from firebase auth")
  return uid

def load_carefulword():
    return CONSTANT.get()
  
try:

  cred = firebase_admin.credentials.Certificate("./firebaseServiceAccountKey.json")
  firebase_admin.initialize_app(cred, options={
    'databaseURL': 'https://revcode-83ac0.firebaseio.com',
  })
  USER = db.reference('user')
  CONSTANT = db.reference('constant')

except:
  print("Get environ key ERROR")
