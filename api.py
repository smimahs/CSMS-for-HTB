from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from app import Charging_process_rate 

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('rate')
parser.add_argument('cdr')


class Charging_Process(Resource):
    def get(self):
        return 'get'

    def post(self):
        data = parser.parse_args()
        result = Charging_process_rate(data)
        return result

api.add_resource(Charging_Process, '/price')

if __name__ == '__main__':
    app.run(debug=True)