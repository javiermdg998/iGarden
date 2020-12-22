# -------------------------------------------------------------------------
#     MQTT PUBLISHER para usar con la App de Android AppMQTT vista en clase
# --------------------------------------------------------------------------
#@Laura Arjona
#@Sistemas Embebidos. 2020
# -----------------------------------
import paho.mqtt.publish as publish
import json
import sys
#MQTT topic
topic = "iGarden/values"

#Dirección del broker
hostname = "test.mosquitto.org"

#---------------------------------------------------
#Leemos los valores del sensor.
# CAMIAD ESTO POR LA LECTURA REAL DEL SENSOR QUE USÉIS
valor = int(sys.argv[1])
#----------------------------------------------
 
# Mensaje que vamos a publicar en el topic definido anteriormente
# El mensaje es un String, en este caso en forma de json
# El envio de un JSON es opcional, se puede enviar simplemente un string.
# #  
# mensaje ={
#   "humedad_suelo": valor,
#   "value":valor
# }
mensaje ={
  "type": "sensors_info",
  "payload": {
    "sensors_info": [
      {
        "id": "salonLuz",
        "name": "Luces del salon",
        "value": True #LECTURA DEL SENSOR
      },

      {
        "id": "salonTemp",
        "name": "Temperatura del salon",
        "value": valor #LECTURA DEL SENSOR
      }
    ]
  }
}
#---------------------------------------------------
# Convertimos el mensaje a JSON
# Publicamos el mensaje
#----------------------------------------------
mensaje_json= json.dumps(mensaje)
publish.single(topic, mensaje_json, hostname=hostname)


print("Mensaje publicado correctamente!")