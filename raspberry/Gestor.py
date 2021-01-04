from enum import Enum
import Invernadero as i
import get_humi_temp as ght
import get_lumi as gl
import time
import salidas
from datetime import datetime
import logger as l
b_marcha = False
i_humedad = 0
i_luminosidad = 0
i_temperatura = 0
b_regado = False
T_MAX = 25
T_MIN = 18
T_NORMAL = 22
PIN_CALEFACTOR = 8
PIN_REFRIGERADOR = 7
PIN_REGADORA = 1 
s_temp_hum = ght.Sensor_temp_hum()
s_lumi = gl.Sensor_lum()

fichero = l.Fichero("/servicio/horas_regado.txt", datetime.today)
H_MIN = 18
H_MAX = 25
H_NORMAL = 22
class Estado(Enum):
    INACTIVO = 0
    INICIAL = 1
    FRIO = 2
    CALIENTE = 3
    SECO = 4
    HUMEDO = 5
    FRIO_HUMEDO = 6
    FRIO_SECO = 7
    CALIENTE_HUMEDO = 8
    CALIENTE_SECO = 9
invernadero = i.Invernadero(i_temperatura, i_humedad, i_luminosidad, b_regado, b_marcha)

def execute():
    e= Estado.INACTIVO
    while True:
        leer(e)
        e = gestionar(e)
        escribir(e)
        time.sleep(0.2)

execute()

def gestionar(estado):
    if estado == estado.INACTIVO:
        if invernadero.marcha == True:
            estado = estado.INICIAL
    elif estado == estado.INICIAL:
        if invernadero.temperatura < T_MIN and invernadero.humedad > H_MIN and invernadero.humedad < H_MAX:
            estado = estado.FRIO
        elif invernadero.temperatura > T_MAX and invernadero.humedad > H_MIN and invernadero.humedad < H_MAX:
            estado = estado.CALIENTE
        elif invernadero.temperatura < T_MIN and invernadero.humedad > H_MAX:
            estado = estado.FRIO_HUMEDO
        elif invernadero.temperatura < T_MIN and invernadero.humedad < H_MIN:
            estado = estado.FRIO_SECO
        elif invernadero.temperatura > T_MAX and invernadero.humedad > H_MAX:
            estado = estado.CALIENTE_HUMEDO
        elif invernadero.temperatura > T_MAX and invernadero.humedad < H_MIN :
            estado = estado.CALIENTE_SECO
    elif estado == estado.FRIO:
        if invernadero.temperatura >= T_NORMAL:
            estado = estado.INICIAL
        elif invernadero.humedad > T_MAX:
            estado = estado.FRIO_HUMEDO
        elif invernadero.humedad < H_MIN:
            estado = estado.FRIO_SECO
    elif estado == estado.CALIENTE:
        if invernadero.temperatura <= T_NORMAL:
            estado = estado.INICIAL
        elif invernadero.humedad > H_MAX:
            estado = estado.CALIENTE_HUMEDO
        elif invernadero.humedad < H_MIN:
            estado = estado.CALIENTE_SECO
    elif estado == estado.HUMEDO:
        if invernadero.humedad <= H_NORMAL:
            estado = estado.INICIAL
        elif invernadero.temperatura > T_MAX:
            estado = estado.CALIENTE_HUMEDO
        elif invernadero.temperatura < T_MIN:
            estado = estado.FRIO_HUMEDO
    elif estado == estado.SECO:
        if invernadero.humedad >= H_NORMAL:
            estado = estado.INICIAL
        elif invernadero.temperatura > T_MAX:
            estado = estado.CALIENTE_SECO
        elif invernadero.temperatura < T_MIN:
            estado = estado.FRIO_SECO
    elif estado == estado.FRIO_HUMEDO:
        if invernadero.humedad <= H_NORMAL and invernadero.temperatura >= T_NORMAL:
            estado = estado.INICIAL
        elif invernadero.temperatura >= T_NORMAL:
            estado = estado.HUMEDO
        elif invernadero.humedad <= H_NORMAL:
            estado = estado.FRIO
    elif estado == estado.FRIO_SECO:
        if invernadero.humedad <= H_NORMAL and invernadero.temperatura >= T_NORMAL:
            estado = estado.INICIAL
        elif invernadero.temperatura >= T_NORMAL:
            estado = estado.SECO
        elif invernadero.humedad >= H_NORMAL:
            estado = estado.FRIO
    elif estado == estado.CALIENTE_HUMEDO:
        if invernadero.humedad <= H_NORMAL and invernadero.temperatura <= T_NORMAL:
            estado = estado.INICIAL
        elif invernadero.temperatura <= T_NORMAL:
            estado = estado.HUMEDO
        elif invernadero.humedad <= H_NORMAL:
            estado = estado.CALIENTE
    elif estado == estado.CALIENTE_SECO:
        if invernadero.humedad >= H_NORMAL and invernadero.temperatura <= T_NORMAL:
            estado = estado.INICIAL
        elif invernadero.temperatura <= T_NORMAL:
            estado = estado.SECO
        elif invernadero.humedad >= H_NORMAL:
            estado = estado.CALIENTE
    return estado
def leer(estado): #FALTA MARCHA
    if estado == estado.INACTIVO:
        invernadero.marcha = True
    elif estado == estado.INICIAL:
        invernadero.humedad, invernadero.temperatura = s_temp_hum.read()
        invernadero.luminosidad = s_lumi.read()
    elif estado == estado.FRIO:
        invernadero.humedad, invernadero.temperatura = s_temp_hum.read()
        invernadero.luminosidad = s_lumi.read()
    elif estado == estado.CALIENTE:
        invernadero.humedad, invernadero.temperatura = s_temp_hum.read()
        invernadero.luminosidad = s_lumi.read()
    elif estado == estado.HUMEDO:
        invernadero.humedad, invernadero.temperatura = s_temp_hum.read()
        invernadero.luminosidad = s_lumi.read()
    elif estado == estado.SECO:
        invernadero.humedad, invernadero.temperatura = s_temp_hum.read()
        invernadero.luminosidad = s_lumi.read()
    elif estado == estado.FRIO_HUMEDO:
        invernadero.humedad, invernadero.temperatura = s_temp_hum.read()
        invernadero.luminosidad = s_lumi.read()
    elif estado == estado.FRIO_SECO:
        invernadero.humedad, invernadero.temperatura = s_temp_hum.read()
        invernadero.luminosidad = s_lumi.read()
    elif estado == estado.CALIENTE_HUMEDO:
        invernadero.humedad, invernadero.temperatura = s_temp_hum.read()
        invernadero.luminosidad = s_lumi.read()    
    elif estado == estado.CALIENTE_SECO:
        invernadero.humedad, invernadero.temperatura = s_temp_hum.read()
        invernadero.luminosidad = s_lumi.read()

def escribir(estado):
    if estado == estado.INACTIVO:
        if b_marcha == True:
            estado = estado.INICIAL
    elif estado == estado.INICIAL:
        print("")
    elif estado == estado.FRIO:
        calentar()
    elif estado == estado.CALIENTE:
        enfriar()
    elif estado == estado.HUMEDO:
        print("HUMEDAD EXCESIVA: " + invernadero.humedad)
    elif estado == estado.SECO:
        activar_regado()
    elif estado == estado.FRIO_HUMEDO:
        calentar()
        print("HUMEDAD EXCESIVA: " + invernadero.humedad)
    elif estado == estado.FRIO_SECO:
        calentar()
        activar_regado()
    elif estado == estado.CALIENTE_HUMEDO:
        enfriar()
        print("HUMEDAD EXCESIVA: " + invernadero.humedad)
    elif estado == estado.CALIENTE_SECO:
        enfriar()
        activar_regado()
def calentar():
    print("ESTOY CALENTANDO")
def desactivar_calentar():
    print("")
def enfriar():
    print("ESTOY ENFRIANDO")
def activar_regado():
    fichero.escribir("- INICIO DE REGADO :" + datetime.now())
    print("ESTOY REGANDO")
def desactivar_regado():
    fichero.escribir("  FIN DE REGADO : " + datetime.now() )
    print("DEJO DE REGAR")