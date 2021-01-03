package es.deusto.embebidos.appmqtt

import android.content.Context
import android.util.Log
import org.eclipse.paho.android.service.MqttAndroidClient
import org.eclipse.paho.client.mqttv3.IMqttActionListener
import org.eclipse.paho.client.mqttv3.IMqttToken
import org.eclipse.paho.client.mqttv3.MqttCallback

class CustomMqttClient(context: Context?, serverURI: String?, clientId: String?) : MqttAndroidClient(context, serverURI, clientId) {

    lateinit var mqttCallback: MqttCallback

    override fun connect(userContext: Any?, callback: IMqttActionListener?): IMqttToken {
        Log.d("MQTT","CONNECTting")
        return super.connect(userContext, callback)
    }

    override fun subscribe(topic: String?, qos: Int, userContext: Any?, callback: IMqttActionListener?): IMqttToken {
        Log.d("MQTT","Subscribing to topic $topic")
        return super.subscribe(topic, qos, userContext, callback)
    }

    override fun setCallback(callback: MqttCallback?) {
        super.setCallback(callback)
        this.mqttCallback = callback!!
    }



}