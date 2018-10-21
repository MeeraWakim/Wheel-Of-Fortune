from flask import Flask, request
from flask_cors import CORS, cross_origin
import sys, os

app = Flask(__name__)

POST_FILE = None

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:8080"}})


@app.route('/uploads/data', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def hello_world():
    global POST_FILE
    if request.method == "POST":
        POST_FILE = request.files['file'].read()
        output_file = open("output.docx", 'wb')
        output_file.write(POST_FILE)
        output_file.close()
        POST_FILE = None
        return 'Good'
    else:
        print "Bad method:", request.method
        return 'Bad'

@app.route('/this-is-so-easy')
def ezpz():
    return "Screw Django"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8081)
