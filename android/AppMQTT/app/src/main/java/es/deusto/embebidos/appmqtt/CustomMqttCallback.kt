package es.deusto.embebidos.appmqtt

import android.content.Context
import android.content.Intent
import android.util.Log
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended
import org.eclipse.paho.client.mqttv3.MqttMessage
import androidx.localbroadcastmanager.content.LocalBroadcastManager


class CustomMqttCallback(val context: Context) : MqttCallbackExtended {
    override fun connectComplete(reconnect: Boolean, serverURI: String?) {
    }

    override fun messageArrived(topic: String?, message: MqttMessage?) {
        Log.d("MQTT","message Arrived")
    }

    override fun connectionLost(cause: Throwable?) {
        log("ConnectionLost ${cause.toString()}")
        LocalBroadcastManager.getInstance(context).sendBroadcast(Intent(SensorsMqttService.CONNECTION_LOST))
    }

    override fun deliveryComplete(token: IMqttDeliveryToken?) {
    }

    private fun log(text: String) {
        Log.d("MQTT", text)
    }
}