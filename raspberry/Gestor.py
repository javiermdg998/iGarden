from enum import Enum
import Invernadero

b_marcha = False
i_humedad = 0
i_luminosidad = 0
i_temperatura = 0
b_regado = False
class Estado(Enum):
    INACTIVO = 0
    INICIAL = 1
    FRIO = 2
    CALIENTE = 3
    SECO = 4
    HUMEDO = 5
invernadero = Invernadero(i_temperatura, i_humedadm, i_luminosidad, b_regado, b_marcha)

def execute(estado):
    if estado == INACTIVO:
        b_marcha = get_marcha()
        if b_marcha == True:
            estado = estado.INICIAL
    elif estado == INICIAL:
        invernadero.humedad = activar_script_humedad
        invernadero.temperatura = activar_script_temperatura
        invernadero.luminosidad = activar_script_luminosidad
        
    elif estado == FRIO:

    elif estado == CALIENTE:

    elif estado == HUMEDO:

    elif estado == SECO: