
package es.deusto.embebidos.appmqtt

import android.app.Service
import android.content.Intent
import android.os.Binder
import android.os.Build
import android.util.Log
import androidx.localbroadcastmanager.content.LocalBroadcastManager
import org.eclipse.paho.client.mqttv3.*
import org.json.JSONObject

class SensorsMqttService : Service() {


    companion object {
        val MQTT_CONNECT = "mqtt_connect"
        val MQTT_DISCONNECT = "mqtt_disconnect"

        //------------------------------------------------------------
        //URL DEL BROKER. DEBE SER EL MISMO BROKER QUE DEFINAIS EN LA RPI
        val MQTT_SERVER_URL = "tcp://test.mosquitto.org"
        //------------------------------------------------------------

        val CONNECTION_SUCCESS = "CONNECTION_SUCCESS"
        val CONNECTION_FAILURE = "CONNECTION_FAILURE"
        val CONNECTION_LOST = "CONNECTION_LOST"
        val DISCONNECT_SUCCESS = "DISCONNECT_SUCCESS"

        val MQTT_MESSAGE_TYPE = "type"
        val MQTT_MESSAGE_PAYLOAD = "payload"

        //------------------------------------------------------------
        //TOPICS. CORRESPONDEN A LOS TOPICS QUE USA LA RPi para publicar
        val TOPICS = arrayOf("iGarden/values")
        //------------------------------------------------------------
    }

    lateinit var mqttClient: CustomMqttClient
    lateinit var mqttCliendId: String


    /**
     * COMIENDO DEL BACKGROUND SERVICE
     */
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {

        this.mqttCliendId = Build.SERIAL

        if(intent == null) {
            stopSelf()
            return Service.START_NOT_STICKY
        }

        if (MQTT_CONNECT == intent.action!!) {
            connectToServer()
        } else if (MQTT_DISCONNECT == intent.action) {
            disconnectFromServer()
        }
        return super.onStartCommand(intent, flags, startId)
    }


    override fun onBind(intent: Intent?) = mBinder

    private val mBinder = LocalBinder()

    inner class LocalBinder : Binder() {
        val service: SensorsMqttService
            get() = this@SensorsMqttService
    }


    /**
     * FUNCION PARA DESCONECTARSE DEL SERVIDOR (BROKER)
     */
     fun disconnectFromServer() {
        this.mqttClient.disconnect(this, object : IMqttActionListener {
            override fun onSuccess(asyncActionToken: IMqttToken?) {
               // logMqtt("Disconnected from server attempt success...")
                mqttClient.unregisterResources()
                SensorsMqttService@ mqttClient.close()
                LocalBroadcastManager.getInstance(this@SensorsMqttService).sendBroadcast(Intent(DISCONNECT_SUCCESS))
                stopSelf()
            }

            override fun onFailure(asyncActionToken: IMqttToken?, exception: Throwable?) {
            }

        })
    }

    /**
     * FUNCION PARA CONECTARSE DEL SERVIDOR (BROKER)
     */
     fun connectToServer() {

        mqttClient = CustomMqttClient(this, MQTT_SERVER_URL, this.mqttCliendId)
        mqttClient.setCallback(CustomMqttCallback(this))

        // enable logs from library
        mqttClient.setTraceEnabled(true)

        val options = MqttConnectOptions()
        options.apply {
            connectionTimeout = 30
            isAutomaticReconnect = true
            isCleanSession = true
            keepAliveInterval = 120
        }

        mqttClient.connect(options,this, object : IMqttActionListener {
            override fun onSuccess(asyncActionToken: IMqttToken?) {
                Log.d("MQTT","Success connecting to server...")

                LocalBroadcastManager.getInstance(this@SensorsMqttService).sendBroadcast(Intent(CONNECTION_SUCCESS))
            }

            override fun onFailure(asyncActionToken: IMqttToken?, exception: Throwable?) {
                LocalBroadcastManager.getInstance(this@SensorsMqttService).sendBroadcast(Intent(CONNECTION_FAILURE))
                Log.d("MQTT","failure connecting to server...")
                disconnectFromServer()
            }
        })
    }

    /**
     * FUNCION PARA SUBSCRIBIRSE A UN TOPIC DETERMINADO
     */
     fun subscribeToTopic(topicName: String, qos: Int, subscriptionListener: IMqttActionListener?, messageListener: IMqttMessageListener?) {
        this.mqttClient.subscribe(topicName, qos, this, subscriptionListener, messageListener)
    }

    /**
     * FUNCION PARA "UNSUBSCRIBE" A UN TOPIC DETERMINADO
     */
     fun unsubscribeFromTopic(topicName: String) {
        this.mqttClient.unsubscribe(topicName)
    }

    /**
     * Publicar un  [MqttMessage] en un determinado [topicName].
     */
    fun publish(topicName: String, message: MqttMessage){
        this.mqttClient.publish(topicName, message, this, object: IMqttActionListener{
            override fun onSuccess(asyncActionToken: IMqttToken?) {
            }

            override fun onFailure(asyncActionToken: IMqttToken?, exception: Throwable?) {
                Log.d("MQTT", "Fail on sending message to topic $topicName")
            }

        })
    }

}