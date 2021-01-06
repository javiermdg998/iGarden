package es.deusto.embebidos.appmqtt

import android.content.*
import android.os.Build
import android.os.Bundle
import android.os.IBinder
import android.util.Log
import android.view.View
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.localbroadcastmanager.content.LocalBroadcastManager
import org.eclipse.paho.client.mqttv3.IMqttActionListener
import org.eclipse.paho.client.mqttv3.IMqttMessageListener
import org.eclipse.paho.client.mqttv3.IMqttToken
import org.eclipse.paho.client.mqttv3.MqttMessage
import org.json.JSONObject
/**
 * SISTEMAS EMBEBIDOS. GRADO DUAL EN INDUSTRIA DIGITAL. 2020
 * App que actúa como publishser o subscriber de MQTT.
 */
class MainActivity : AppCompatActivity() {

    private var mqttService: SensorsMqttService? = null
    private lateinit var mqttBroadcast: MqttBroadcast
//    lateinit var dataFromPublisher :TextView
    lateinit var temperatura_view :TextView
    lateinit var humid_view :TextView
    lateinit var humidity_view :TextView
    lateinit var luminity_view :TextView


    /**
     * FUNCION QUE SE EJECUTA AL INICIAR LA APP
     */
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        temperatura_view=findViewById<TextView>(R.id.lbl_temperatura)

//        dataFromPublisher         = findViewById<TextView>(R.id.textoXML)
//        dataFromPublisher.text = "EJEMPLO DE MQTT"

        humid_view=findViewById<TextView>(R.id.lbl_humid)
        humidity_view=findViewById<TextView>(R.id.lbl_humidity)
        luminity_view=findViewById<TextView>(R.id.lbl_luz)

        mqttBroadcast = MqttBroadcast()
        initMqttService(View(this))
    }

    // --------------------------------------------------------------------
    val serviceConnection = object: ServiceConnection {
        override fun onServiceConnected(name: ComponentName?, service: IBinder?) {
            mqttService = (service as SensorsMqttService.LocalBinder).service
        }

        override fun onServiceDisconnected(name: ComponentName?) {
            mqttService = null
        }
    }
    // ---------------------------------------------------------------------

    /**
     * Función que se llama al pulsar el botón del XML para conectar
     * Se conecta al broker, y se subscribe al topic  TOPICS[0], definido
     * en la clase SensorsMqttService.kt, línea 35
     */
    fun initMqttService(v: View) {
        LocalBroadcastManager.getInstance(this).registerReceiver(mqttBroadcast, IntentFilter(SensorsMqttService.CONNECTION_SUCCESS))

        val startServiceIntent = Intent(this, SensorsMqttService::class.java)
        this.bindService(startServiceIntent, serviceConnection, 0)

        startServiceIntent.action = SensorsMqttService.MQTT_CONNECT

        if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            this.startService(startServiceIntent)
        } else {
            this.startService(startServiceIntent)
        }

    }


    /**
     * Función para SUBSCRIBIRSE a un determinado  topic
     */
    fun subsTopic() {
        mqttService?.subscribeToTopic(SensorsMqttService.TOPICS[0], 0, object : IMqttActionListener {
            override fun onSuccess(asyncActionToken: IMqttToken?) {

                Log.d("MQTT", "EXITO EN LA SUBSCRIPCION AL TOPIC ${SensorsMqttService.TOPICS[0]}")
            }

            override fun onFailure(asyncActionToken: IMqttToken?, exception: Throwable?) {
                Log.d("MQTT", "ERROR EN LA SUBSCRIPCION ")
            }
        }, IMqttMessageListener { topic, message ->

            val msgObj = JSONObject(message.toString())
            println("-----------------------------------------------")
            println(msgObj)
            println(message)
            println("----------------------------------------------")


            val humedad=msgObj.getDouble(SensorsMqttService.MQTT_MESSAGE_HUMEDAD)
            val temperatura=msgObj.getDouble(SensorsMqttService.MQTT_MESSAGE_TEMPERATURA)
            val luminosidad=msgObj.getDouble(SensorsMqttService.MQTT_MESSAGE_LUMINOSIDAD)
            val humedo=msgObj.getBoolean(SensorsMqttService.MQTT_MESSAGE_HUMEDO)
            println(humedad)
            println(temperatura)
            println("----------------------------------------------")
            var txt_humedo=""
            if(humedo){
                txt_humedo="SI"
            }else{
                txt_humedo="NO"
            }
            runOnUiThread {
                        humidity_view.text=humedad.toString() +" %"
                        temperatura_view.text= temperatura.toString() +" ºC"
                        luminity_view.text=luminosidad.toString() + " lux"
                        humid_view.text=txt_humedo
            }
//            when(type){
//
//                "sensors_info" -> {
//                    val array = payload.getJSONArray("sensors_info")
//                    val tempSalon = array.getJSONObject(1).get("value")
//                    val temp2 = array.getJSONObject(0).get("value")
//                    runOnUiThread {
//                        dataFromPublisher.text = "Temperatura salon = " + tempSalon.toString()
//                        temperatura_view.text=temp2.toString()
//                    }
//                }
//            }

        })


    }


    // ---------------------------------------------------------------------
    /**
     * Función para PUBLICAR topic
     */
    fun publishTopic(){
        val message = MqttMessage()
        val jsonMessage = JSONObject()
        val sensorInfo = JSONObject()
        jsonMessage.put(SensorsMqttService.MQTT_MESSAGE_TYPE, "SENSORS_INFO")

        //MENSAJE A PUBLICAR. lO INCORPORAMOS EN UN JSON
        sensorInfo.put("id", "salonLuz")
        sensorInfo.put("value", false)

        jsonMessage.put("sensor_info", sensorInfo)

        message.qos = 0
        message.payload = jsonMessage.toString().toByteArray()

        // here we ask for home sensors information
       mqttService!!.publish(SensorsMqttService.TOPICS[0], message)

    }

    // ---------------------------------------------------------------------

     fun stopMqttService() {
        this.unbindService(serviceConnection)
        LocalBroadcastManager.getInstance(this).unregisterReceiver(mqttBroadcast)
        val startServiceIntent = Intent(this, SensorsMqttService::class.java)
        startServiceIntent.action = SensorsMqttService.MQTT_DISCONNECT
        this.startForegroundService(startServiceIntent)

    }
    // ---------------------------------------------------------------------



// ---------------------------------------------------------------------
    inner class MqttBroadcast: BroadcastReceiver() {
    //Esta función se llaman automáticamente cuando hay CAMBIOS en la conexión MQTT con el broker
    override fun onReceive(context: Context?, intent: Intent?) {
        //Esta condició se ejecuta automáticamente cuando la conexión con el broker tiene éxito
            if(SensorsMqttService.CONNECTION_SUCCESS == intent!!.action){
                 subsTopic()
            }

            if(SensorsMqttService.CONNECTION_FAILURE == intent.action){

            }

            if(SensorsMqttService.CONNECTION_LOST == intent.action){

            }

            if(SensorsMqttService.DISCONNECT_SUCCESS == intent.action){
                stopMqttService()
            }
        }

    }
}