from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_api

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "Working"

@app.route('/adduser', methods = ['POST'])
def adduser():
    try:
        if request.method == 'POST':
            # uid = request.args.get("uid")
            # username = request.args.get("uname")
            # print("got args")
            data = request.json
            firebase_api.add_new_user(data["uid"], data["name"])
            return jsonify({"status": "ok",
                            "uid": data["uid"]})
    except:
        return jsonify({"status": "error"})

@app.route('/userdata', methods = ['GET'])
def getUserData():
    try:
        if request.method == 'GET':
            uid = request.args.get("uid")
            return jsonify({"status": "ok",
                            "uid": uid,
                            "userData": firebase_api.get_user_data(uid)})
    except:
        return jsonify({"status": "error"})
    
@app.route('/speech', methods=['GET', 'POST'])
def getSpeech():
    data = request.get_json()
    try:
        print(data['res'])
    except:
        print("error")
    return "running"

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)