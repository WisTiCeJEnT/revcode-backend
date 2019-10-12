from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_api

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "Working"

@app.route('/adduser', methods = ['POST'])
def add_user():
    # try:
        if request.method == 'POST':
            # uid = request.args.get("uid")
            # username = request.args.get("uname")
            # print("got args")
            data = request.get_json()
            firebase_api.add_new_user(data["uid"], data["name"])
            return jsonify({"status": "ok",
                            "uid": data["uid"]})
    # except:
        # return jsonify({"status": "error"})

@app.route('/userdata', methods = ['GET'])
def get_user_data():
    try:
        if request.method == 'GET':
            uid = request.args.get("uid")
            return jsonify({"status": "ok",
                            "uid": uid,
                            "userData": firebase_api.get_user_data(uid)})
    except:
        return jsonify({"status": "error"})

@app.route('/loadfile', methods = ['GET'])
def user_load_file():
    try:
        uid = request.args.get("uid")
        file_id = request.args.get("file_id")
        return jsonify({"status": "ok",
                        "uid": uid,
                        "file_data": firebase_api.get_file(uid, file_id)})
    except:
        return jsonify({"status": "error"})

@app.route('/newfile', methods = ['GET'])
def user_add_new_file():
    try:
        uid = request.args.get("uid")
        return jsonify({"status": "ok",
                        "uid": uid,
                        "file_id": firebase_api.add_new_file(uid)})
    except:
        return jsonify({"status": "error"})
        
@app.route('/savefile', methods = ['POST'])
def user_save_file():
    try:
        data = request.get_json()
        return jsonify({"status": "ok",
                        "uid": data["uid"],
                        "file_id": firebase_api.save_file(data["uid"], data["file_id"], data)})
    except:
        return jsonify({"status": "error"})

@app.route('/removefile', methods = ['POST'])
def user_remove_file():
    try:
        data = request.json
        return jsonify({"status": "ok",
                        "uid": data["uid"],
                        "file_id": firebase_api.remove_file(data["uid"], data["file_id"])})
    except:
        return jsonify({"status": "error"})

@app.route('/speech', methods = ['GET', 'POST'])
def getSpeech():
    data = request.get_json()
    try:
        print(data['res'])
    except:
        print("error")
    return "running"

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)