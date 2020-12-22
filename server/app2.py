from flask import Flask, jsonify, render_template
from data.db import Database
from flask_socketio import SocketIO
from flask_cors import CORS
import json


app = Flask(__name__)
cors = CORS(app, resources={r"/**": {"origins": "*"}},)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, port=2345)

@socketio.on("connect")
def connected():
    print("user connected")


@socketio.on("disconnect")
def disconnected():
    print("user disconnected")

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

db=Database()
@app.route('/')
def hello_world():
    obj=db.select()
    data=[]
    for x in obj:
        data.append({
            "value":x[1],
            "time":str(x[2])
        })  
        
    return jsonify(data)


@app.route('/<valor>', methods=['GET'])
def mostrar_valor(valor):
    return valor
    
if __name__ == '__main__':
    app.debug=True
    socketio.run(app,port=2345)