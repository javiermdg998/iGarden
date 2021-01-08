from enum import Enum
import Invernadero as i
import get_humi_temp as ght
import get_lumi as gl
import soil as sl
import time
import salidas
from datetime import datetime
import smbus
import dht_config
import paho.mqtt.publish as publish
import json
import sys
import logger as l
import RPi.GPIO as GPIO
b_marcha = False
i_humedad = 0
i_luminosidad = 0
i_temperatura = 0
b_regado = False
T_MAX = 25
T_MIN = 18
T_NORMAL = 22
PIN_CALEFACTOR = 8 #azul
PIN_REFRIGERADOR = 7 #rojo
PIN_REGADORA = 25 #verde

s_temp_hum = ght.Sensor_temp_hum()
s_lumi = gl.Sensor_lum()
s_regado = sl.Sensor_moisture()
calefactor = salidas.Led(PIN_CALEFACTOR)
refrigerador = salidas.Led(PIN_REFRIGERADOR)
regadora = salidas.Led(PIN_REGADORA)
fichero = l.Fichero("/home/pi/Desktop/raspberry/servicio/horas_regado.txt", str(datetime.today()))
R_TRUE = True
R_FALSE = False
class Estado(Enum):
    INACTIVO = 0
    INICIAL = 1
    FRIO = 2
    CALIENTE = 3
    SECO = 4
    FRIO_SECO = 5
    CALIENTE_SECO = 6

invernadero = i.Invernadero(i_temperatura, i_humedad, i_luminosidad, b_regado, b_marcha)

t_seco_inicial = False
t_inicial_seco = False

def gestionar(estado):
    global t_seco_inicial
    global t_inicial_seco
    if estado == estado.INACTIVO:
        if invernadero.marcha == True:
            estado = estado.INICIAL
    elif estado == estado.INICIAL:
        if invernadero.temperatura < T_MIN and invernadero.regado == R_TRUE:
            estado = estado.FRIO
        elif invernadero.temperatura > T_MAX and invernadero.regado == R_TRUE:
            estado = estado.CALIENTE
        elif invernadero.temperatura < T_MIN and invernadero.regado == R_FALSE:
            estado = estado.FRIO_SECO
            t_inicial_seco = True
        elif invernadero.temperatura > T_MAX and invernadero.regado == R_FALSE:
            t_inicial_seco = True
            estado = estado.CALIENTE_SECO
    elif estado == estado.FRIO:
        if invernadero.temperatura >= T_NORMAL:
            estado = estado.INICIAL
        elif invernadero.regado == R_FALSE:
            estado = estado.FRIO_SECO
            t_inicial_seco = True
    elif estado == estado.CALIENTE:
        if invernadero.temperatura <= T_NORMAL:
            estado = estado.INICIAL
        elif invernadero.regado == R_FALSE:
            estado = estado.CALIENTE_SECO
            t_inicial_seco = True
    elif estado == estado.SECO:
        if invernadero.regado == R_TRUE:
            estado = estado.INICIAL
            t_seco_inicial = True
        elif invernadero.temperatura > T_MAX:
            estado = estado.CALIENTE_SECO
        elif invernadero.temperatura < T_MIN:
            estado = estado.FRIO_SECO
    elif estado == estado.FRIO_SECO:
        if invernadero.regado == R_TRUE and invernadero.temperatura >= T_NORMAL:
            estado = estado.INICIAL
            t_seco_inicial = True
        elif invernadero.temperatura >= T_NORMAL:
            estado = estado.SECO
        elif invernadero.regado == R_TRUE:
            estado = estado.FRIO
            t_seco_inicial = True
    elif estado == estado.CALIENTE_SECO:
        if invernadero.regado == R_TRUE and invernadero.temperatura <= T_NORMAL:
            estado = estado.INICIAL
            t_seco_inicial = True
        elif invernadero.temperatura <= T_NORMAL:
            estado = estado.SECO
        elif invernadero.regado == R_TRUE:
            estado = estado.CALIENTE
            t_seco_inicial = True
    return estado

def leer(estado): #FALTA MARCHA
    if estado == estado.INACTIVO:
        invernadero.marcha = True
    elif estado != estado.INACTIVO:
        invernadero.humedad, invernadero.temperatura = s_temp_hum.read()
        #invernadero.humedad = int(input("Introduce humedad : "))
        #invernadero.temperatura = int(input("Introduce temperatura : " ))
        invernadero.luminosidad = s_lumi.read()
        invernadero.regado = s_regado.read()
    
def escribir(estado):
    if estado == estado.INACTIVO:
        if b_marcha == True:
            estado = estado.INICIAL
    elif estado == estado.INICIAL:
        desactivar_calentar()
        desactivar_enfriar()
        desactivar_regado()
        print("")
    elif estado == estado.FRIO:
        desactivar_enfriar()
        desactivar_regado()
        calentar()
    elif estado == estado.CALIENTE:
        desactivar_calentar()
        desactivar_regado()
        enfriar()
    elif estado == estado.SECO:
        desactivar_calentar()
        desactivar_enfriar()
        activar_regado()
    elif estado == estado.FRIO_SECO:
        calentar()
        desactivar_enfriar()        
        activar_regado()
    elif estado == estado.CALIENTE_SECO:
        enfriar()
        activar_regado() 
        desactivar_calentar()

    dateTimeObj = datetime.now()
    dateTimeObj=str(dateTimeObj)
    topic = "iGarden/values" 
    hostname = "test.mosquitto.org"

    mensaje ={
     "humedad":invernadero.humedad,
     "temperatura":invernadero.temperatura,
     "luminosidad":invernadero.luminosidad,
     "fecha":dateTimeObj,
     "humid":invernadero.regado
    }
    mensaje_json= json.dumps(mensaje)
    publish.single(topic, mensaje_json, hostname=hostname)
    print(mensaje)
    
def calentar():
    print("CALENTANDO")
    calefactor.encender_led()
def desactivar_calentar():
    print("YA NO CALENTANDO")
    calefactor.apagar_led()
def enfriar():
    print("ENFRIANDO")
    refrigerador.encender_led()
def desactivar_enfriar():
    print("YA NO ENFRIANDO\n")
    refrigerador.apagar_led()
def activar_regado():
    print("REGANDO")
    global t_inicial_seco
    regadora.encender_led()
    print("REGANDO\n")
    if t_inicial_seco == True:
        fichero.escribir("\n- INICIO DE REGADO :" + str(datetime.now()) + "\n")
        t_inicial_seco = False
def desactivar_regado():
    print("YA NO REGANDO")
    global t_seco_inicial
    regadora.apagar_led()
    if t_seco_inicial == True:
        fichero.escribir("  FIN DE REGADO : " + str(datetime.now()) + "\n")
        t_seco_inicial = False

def execute():
    GPIO.cleanup()
    e= Estado.INACTIVO
    while True:
        leer(e)
        e = gestionar(e)
        escribir(e)
        print("HUMEDAD = " + str(invernadero.humedad) + " | TEMP = " + str(invernadero.temperatura) + " | ESTADO = " + str(e)) 
        time.sleep(2)

execute()