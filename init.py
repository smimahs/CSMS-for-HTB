from flask import render_template,redirect
import api
from config import app

@app.route('/', methods=['GET'])
def home():
    return render_template('CSMS.html')

if __name__ == '__main__':
    app.run(debug=True)