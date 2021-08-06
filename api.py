from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from app import Charging_process_rate 
import json


app = Flask(__name__)
api = Api(app)


class Charging_Process(Resource):
    def get(self):
        return 'get'

    def post(self):
        return str(request.form.get)
        result = Charging_process_rate(request.form)
        return result

api.add_resource(Charging_Process, '/price')

if __name__ == '__main__':
    app.run(debug=True)