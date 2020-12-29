import eventlet
import json
from flask import Flask, render_template,jsonify
from flask_mqtt import Mqtt
from flask_socketio import SocketIO, emit
from data.db import Database
from flask_cors import CORS

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET'] = 'my secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'test.mosquitto.org'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False


mqtt = Mqtt(app)
db=Database()
socketio = SocketIO(app,cors_allowed_origins="*",engineio_logger=True, logger=True)
CORS(app,resources={r"/*":{"origins":"*"}} )
mqtt.subscribe('iGarden/values')
# Parameters for SSL enabled
# app.config['MQTT_BROKER_PORT'] = 8883
# app.config['MQTT_TLS_ENABLED'] = True
# app.config['MQTT_TLS_INSECURE'] = True
# app.config['MQTT_TLS_CA_CERTS'] = 'ca.crt'

state={
    "humidity":0,
    "temperature":0,
    "humid":True,
    "lightness":0
}


@app.route('/state')
def get_state(): 
    print(state) 
    return jsonify(state)

@app.route('/')
def index():
    emit('message',{"data":"hellos"})
    return render_template('index.html')

@app.route('/temperature')
def get_temperature():
    data=db.select_temperatures()
    return jsonify(data)

@app.route('/humidity')
def get_humidity():
    data=db.select_humidity()
    return jsonify(data)

@app.route('/luminity')
def get_luminities():
    data=db.select_luminities()
    return jsonify(data)


@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'])


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('subscribe')#prescindible
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'])


@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(data)
    payload=data["payload"]
    values=json.loads(payload)
    
    state["humidity"] = values["humedad"]
    state["temperature"] = values["temperatura"]
    state["lightness"] = values["luminosidad"]
    socketio.emit('mqtt_message', data=data)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('iGarden/values')

if __name__ == '__main__':
    app.debug=True
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)