# iGarden

iGarden es un sistema de monitorización remoto para un invernadero.
El sistema esta formado por:

 - Aplicación Python en una RaspberryPi que controla el invernadero
 - Aplicación Android que visualiza los datos
 - Aplicación Flask que registra los datos
 - Aplicación Vue que visualiza los datos
 ![enter image description here](https://github.com/javiermdg998/iGarden/blob/main/diagramas/diagrama.png?raw=true)
 ## Raspberry
 La Raspberry será la encargada de controlar la temperatura del invernadero y humedad del suelo, basándose en en la información que recogerá a través de los sensores.
 Además se encargará de enviar los datos que recava a la nube MQTT de Mosquitto de donde serán escuchados por el servidor Flask y la aplicación Android.
### Conexiones
![enter image description here](https://github.com/javiermdg998/iGarden/blob/main/diagramas/conexiones.png?raw=true) 


 
 ## Android
 Esta sencilla aplicación Android escuchara al 'topic' *iGarden/values* de la nube de mosquitto y se los visualizará al usuario
 
## Flask
La aplicación Flask escuchara los datos enviados por el invernadero y los almacenará en una base de datos MySQL, además también se encargará de proporcionar el registro de datos como el estado actual del invernadero a la aplicación Vue.

## Vue
Esta aplicación servirá de dashboard para el invernadero ya que desde aquí podremos visualizar el historial de registros del invernadero como el estado en tiempo real del mismo

