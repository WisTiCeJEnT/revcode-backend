from flask import Flask, request, jsonify
from flask_cors import CORS

import sys
import json
import traceback

sys.path.insert(1, './TexttoCode')
import grammar
import firebase_api


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def root():
    return "Working"

@app.route('/adduser', methods = ['POST'])
def add_user():
    try:
        if request.method == 'POST':
            data = request.get_json()
            data["filename"] = "HowTo.txt"
            data["extension"] = "txt - Text file"
            data["code"] = ['', '### File Handling ###', '#1.Create new file on add button', '#2.Choose your file to edit', '#3.Edit your file', '#4.Save file on save button', '#5.Delete file on delete button ', '#\t( Note that your file will be removed permanently )', '', '### Speech Feature ###', '#1.Click or press on microphone button to turn this feature on', '#2.You must to allow browser to access your microphone', '#3.Speak your code', '#4.RevCode will process your speech and generate it into real code', '#5.Turn this feature off by clicking on microphone button again', '', '### Enjoy Coding ### ', '']
            firebase_api.add_new_user(data["uid"], data["name"], data["email"])
            file_id = firebase_api.add_new_file(data)
            firebase_api.save_file(data["uid"], file_id, data)
            return jsonify({"status": "ok",
                            "uid": data["uid"],
                            "file_id": file_id})
    except Exception as e: 
        print("Error:", e)
        traceback.print_exc()
        return jsonify({"status": "error"})

@app.route('/userdata', methods = ['GET'])
def get_user_data():
    try:
        if request.method == 'GET':
            uid = request.args.get("uid")
            return jsonify({"status": "ok",
                            "uid": uid,
                            "userData": firebase_api.get_user_data(uid)})
    except Exception as e: 
        print("Error:", e)
        traceback.print_exc()
        return jsonify({"status": "error"})

@app.route('/loadfile', methods = ['GET'])
def user_load_file():
    try:
        uid = request.args.get("uid")
        file_id = request.args.get("file_id")
        return jsonify({"status": "ok",
                        "uid": uid,
                        "file_data": firebase_api.get_file(uid, file_id)})
    except Exception as e: 
        print("Error:", e)
        traceback.print_exc()
        return jsonify({"status": "error"})

@app.route('/newfile', methods = ['POST'])
def user_add_new_file():
    try:
        data = request.get_json()
        return jsonify({"status": "ok",
                        "uid": data["uid"],
                        "file_id": firebase_api.add_new_file(data)})
    except Exception as e: 
        print("Error:", e)
        traceback.print_exc()
        return jsonify({"status": "error"})
        
@app.route('/savefile', methods = ['POST'])
def user_save_file():
    try:
        data = request.get_json()
        return jsonify({"status": "ok",
                        "uid": data["uid"],
                        "file_id": firebase_api.save_file(data["uid"], data["file_id"], data)})
    except Exception as e: 
        print("Error:", e)
        traceback.print_exc()
        return jsonify({"status": "error"})

@app.route('/removefile', methods = ['POST'])
def user_remove_file():
    try:
        data = request.json
        return jsonify({"status": "ok",
                        "uid": data["uid"],
                        "file_id": firebase_api.remove_file(data["uid"], data["file_id"])})
    except Exception as e: 
        print("Error:", e)
        return jsonify({"status": "error"})

@app.route('/removeuser', methods = ['POST'])
def remove_user():
    try:
        data = request.json
        return jsonify({"status": "ok",
                        "uid": firebase_api.remove_user(data["uid"])})
    except Exception as e: 
        print("Error:", e)
        traceback.print_exc()
        return jsonify({"status": "error"})

@app.route('/speech', methods = ['GET', 'POST'])
def getSpeech():
    try:
        if request.method == 'POST':
            data = request.json
            text = data["raw_text"]
            current_indent = firebase_api.get_indent(data["uid"], data["file_id"], data["line_no"])
            revcode, new_indent, just_cut, before_detext = grammar.grammar(text, current_indent)
            firebase_api.set_indent(data["uid"], data["file_id"], data["line_no"], new_indent, revcode)
            print(json.dumps({"status": "ok",
                            "before_text": text,
                            "cut_text": just_cut,
                            "before_detect": before_detext,
                            "code": revcode}, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))

            return jsonify({"status": "ok",
                            "before_text": text,
                            "cut_text": just_cut,
                            "before_detect": before_detext,
                            "code": revcode})

        else:
            text = request.args.get("text")
            revcode, new_indent, just_cut, before_detext = grammar.grammar(text, 0)
            return jsonify({"status": "ok",
                            "before_text": text,
                            "cut_text": just_cut,
                            "before_detect": before_detext,
                            "code": revcode})
    except Exception as e: 
        print("Error:", e)
        traceback.print_exc()
        return jsonify({"status": "error"})

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
