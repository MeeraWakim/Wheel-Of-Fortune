from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sys, os
from resume_check import ResumeParse

app = Flask(__name__)

POST_FILE = None

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = '/downloads/data'

#cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:8080"}})
cors = CORS(app, resources={r"/uploads/data": {"origins": "http://localhost:8080"}})


@app.route('/uploads/data', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def read_file():
    global POST_FILE
    if request.method == "POST":
        POST_FILE = request.files['file'].read()
        output_file = open("output.docx", 'wb')
        output_file.write(POST_FILE)
        output_file.close()
        POST_FILE = None
        rp = ResumeParse("output.docx")
        #file_output = {"basic": rp.check_basic(), "spelling": rp.check_spelling, "tense": rp.check_tense} #The Tense return of the resume_checker
        file_output = {"basic": rp.check_basic(), "spelling": {}, "tense": {}}
        return jsonify(file_output)
    else:
        print("Bad method:", request.method)
        return 'Bad'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8081)
