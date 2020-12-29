from enum import Enum

b_marcha = False
i_humedad = 0
i_luminosidad = 0
i_temperatura = 0

class Estado(Enum):
    INICIAL = 0
    RECOGIENDO_DATOS = 1
    FRIO = 2
    CALIENTE = 3
    SECO = 4
    HUMEDO = 5

def get_marcha():
    return True
def get_humedad():
    return 0
def get_luminosidad():
    return 0
def get_temperatura():
    return 0
def gestionar(estado):
    if estado == INICIAL:
        b_marcha = get_marcha()
        if b_marcha == True:
            estado = estado.RECOGIENDO_DATOS
    elif estado == RECOGIENDO_DATOS:
        i_humedad = get_humedad()
        i_temperatura = get_temperatura()
        i_luminosidad = get_luminosidad()
    elif estado == FRIO:

    elif estado == CALIENTE:

    elif estado == HUMEDO:

    elif estado == SECO: