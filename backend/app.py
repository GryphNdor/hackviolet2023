from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse
import werkzeug
import subprocess

import os
from pathlib import Path

app = Flask(__name__)
CORS(app, origin="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Origin"],
    supports_credentials=True)
api = Api(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config["UPLOAD_FOLDER"] = "static/"

class FileHandler(Resource):
    def post(self):

        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('name', type=str, location='form')
        args = parse.parse_args()
        image_file = args['file']
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg'))
        name = args['name']
        with open(app.config["UPLOAD_FOLDER"]+"/name.txt", "w") as f:
            f.write(name);

        fileDict = {}

        urls = []
        truths = []

        with open('truthtable.txt', 'r') as file:
            truths = file.readlines() 

        with open('allURLS.txt', 'r') as file:
            urls = file.readlines() 
        
        for i in range(len(urls) -1):
            fileDict[urls[i]] = truths[i]

        return fileDict


api.add_resource(FileHandler, '/submit', endpoint='submit')
api.add_resource(FileHandler, '/data', endpoint='data')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)