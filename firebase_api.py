import pyrebase
import datetime
import os

def add_new_user(uid, name):
  if(uid not in dict(db.child("user").get().val()).keys()):
      data = {
        "user_data": {
          "uid": uid, 
          "name": name
          },
        "user_storage": {}
      }
      db.child("/user/").child(uid).set(data)

def get_user_data(uid):
  db_data = db.child("user").child(uid).get().val()
  res = {}
  res["user_data"] = db_data["user_data"]
  res["user_storage"] = []
  for item in db_data["user_storage"].keys():
    tmp = {}
    tmp["filename"] = db_data["user_storage"][item]["filename"]
    tmp["extension"] = db_data["user_storage"][item]["extension"]
    tmp["last_edit"] = db_data["user_storage"][item]["date_edit"]
    tmp["file_id"] = item
    res["user_storage"].append(tmp)
  return res

def get_file(uid, file_id):
  db_data = db.child("user").child(uid).child("user_storage").child(file_id).get().val()
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
  item_id = db.child("user").child(uid).child("user_storage").push(data)
  return item_id["name"]

def save_file(uid, file_id, file_data):
  data = db.child("user").child(uid).child("user_storage").child(file_id).get().val()
  data["code"] = file_data["code"]
  data["extension"] = file_data["extension"]
  data["filename"] = file_data["filename"]
  data["date_edit"] = datetime.datetime.now().strftime("%d-%m-%Y")
  item_id = db.child("user").child(uid).child("user_storage").child(file_id).set(data)
  return item_id["name"]

def remove_file(uid, file_id):
  item_id = db.child("user").child(uid).child("user_storage").child(file_id).remove()
  return item_id["name"]
  


try:
  config = {
    "apiKey": os.environ.get("FIREBASE_APIKEY"),
    "authDomain": "https://revcode-83ac0.firebaseapp.com/",
    "databaseURL": "https://revcode-83ac0.firebaseio.com/",
    "storageBucket": "projectId.appspot.com",
    #"serviceAccount": ""
  }

  firebase = pyrebase.initialize_app(config)
  db = firebase.database()

except:
  print("Get environ key ERROR")
