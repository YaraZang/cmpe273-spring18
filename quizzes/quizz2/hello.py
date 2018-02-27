from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)

USER_MAP = {}
id = 1

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def new_users():
    global USER_MAP
    global id
    name = request.form["name"]
    USER_MAP[id] = name
    data = {
        'id': id,
        'name': name
    }
    response = app.response_class(
        response=json.dumps(data),
        status=201,
        mimetype='application/json'
    )
    id = id + 1
    return response

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    global USER_MAP
    response = 0
    if id in USER_MAP.keys():
        name = USER_MAP[id]
        data = {
        'id': id,
        'name': name
        }
        response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    else:
        response = app.response_class(
        response="not found",
        status=404,
        mimetype='application/text'
    )
    return response


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global USER_MAP
    response = 0
    if id in USER_MAP.keys():
        del USER_MAP[id]
        response = app.response_class(
        response='',
        status=204,
        mimetype='application/text'
        )
    else:
        response = app.response_class(
        response="no such user",
        status=404,
        mimetype='application/text'
        )
    return response


    
