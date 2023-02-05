from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse
import werkzeug

import os
import json

app = Flask(__name__)
CORS(app, origin="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Origin"],
    supports_credentials=True)
api = Api(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config["UPLOAD_FOLDER"] = "static/"

todos = {}

class FileHandler(Resource):
    def post(self):

        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        image_file = args['file']
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename))
        name = args['name']


api.add_resource(FileHandler, '/submit', endpoint='submit')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)