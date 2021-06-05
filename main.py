from flask import Flask, Response, request
from db_api import persistMessage, getMessage
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/view', methods = ['POST'])
def viewMessage():
    try:
        if request.method == 'POST':
            password = request.json['password']
            message = getMessage(password)

            if message == 'Non-Existent':
                error = {'message': 'No message exists for this password'}
                return Response(error, status=204, mimetype='application/json')

            return {'data': message}
    except Exception as e:
        print(e)

@app.route('/send', methods = ['POST'])
def sendMessage():
    try:
        if request.method == 'POST':
            password = request.json['password']
            message = request.json['message']

            status = persistMessage(password, message)
            
            if status == 'Already Exists':
                error = {'message': 'Password is already in use'}
                return Response(error, status=409, mimetype='application/json')

            return {'data': status}
    except Exception as e:
        print(e)

if __name__ == "__main__":
    """ This is to be used for development purposes only"""
    app.run()