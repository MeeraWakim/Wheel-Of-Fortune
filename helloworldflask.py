from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/uploads/data',methods=['GET','POST'])

def helowurld():
        return (request.method)