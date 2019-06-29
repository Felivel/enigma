from flask import Flask, render_template, jsonify
import hashlib
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/square/<int:number>')
def square(number):
    response = jsonify({'result': number*number})
    response.status_code = 200
    return response

@app.route('/uuid')
def generate_uuid():
    result = str(uuid.uuid4())
    response = jsonify({'result': result})
    response.status_code = 200
    return response

@app.route('/sha1/<string:text>')
def sha1(text):
    result = hashlib.sha1(text.encode())
    response = jsonify({'result': result.hexdigest()})
    response.status_code = 200
    return response

@app.route('/sha256/<string:text>')
def sha256(text):
    result = hashlib.sha256(text.encode())
    response = jsonify({'result': result.hexdigest()})
    response.status_code = 200
    return response