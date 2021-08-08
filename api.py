from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from app import Charging_process_rate 
from flask import render_template,redirect

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('rate')
parser.add_argument('cdr')

# load ui for testing
@app.route('/rate', methods=['GET'])
def home():
    return render_template('CSMS.html')

# Rate post API for charging process ratting    
class Charging_Process(Resource):
    def post(self):
        data = parser.parse_args()
        result = Charging_process_rate(data)
        return result

api.add_resource(Charging_Process, '/rate')

if __name__ == '__main__':
    app.run(debug=True)