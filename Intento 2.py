from machine import Pin, ADC
import time

# Definir los pines para los LEDs del primer semáforo vehicular
led_rojo_1 = Pin(15, Pin.OUT)
led_amarillo_1 = Pin(2, Pin.OUT)
led_verde_1 = Pin(4, Pin.OUT)

# Definir los pines para los LEDs del segundo semáforo vehicular
led_rojo_2 = Pin(27, Pin.OUT)
led_amarillo_2 = Pin(26, Pin.OUT)
led_verde_2 = Pin(25, Pin.OUT)

# Definir los pines para los LEDs del tercer semáforo vehicular
led_rojo_3 = Pin(22, Pin.OUT)
led_amarillo_3 = Pin(21, Pin.OUT)
led_verde_3 = Pin(19, Pin.OUT)

# Definir los pines para los LEDs del primer semáforo peatonal
peatonal_rojo_1 = Pin(16, Pin.OUT)
peatonal_verde_1 = Pin(17, Pin.OUT)

# Definir los pines para los LEDs del segundo semáforo peatonal
peatonal_rojo_2 = Pin(14, Pin.OUT)
peatonal_verde_2 = Pin(13, Pin.OUT)

# Definir el pulsador para el cruce peatonal
pulsador = Pin(12, Pin.IN, Pin.PULL_UP)

# Definir el pulsador para activar el sensor de temperatura
temp_pulsador = Pin(33, Pin.IN, Pin.PULL_UP)

# Configurar el sensor LM35 en un pin analógico
sensor_temp = ADC(Pin(32))
sensor_temp.atten(ADC.ATTN_11DB)  # Rango de 0 a 3.3V

# Variables de control
solicitar_cruce = False
modo_temperatura = False

def interrupcion_pulsador(pin):
    global solicitar_cruce
    solicitar_cruce = True

def interrupcion_temp_pulsador(pin):
    global modo_temperatura
    modo_temperatura = not modo_temperatura  # Alterna entre encendido y apagado

# Configurar interrupciones
pulsador.irq(trigger=Pin.IRQ_FALLING, handler=interrupcion_pulsador)
temp_pulsador.irq(trigger=Pin.IRQ_FALLING, handler=interrupcion_temp_pulsador)

while True:
    if modo_temperatura:
        print("Modo temperatura activado.")
        while modo_temperatura:
            lectura = sensor_temp.read()  # Leer valor analógico
            voltaje = lectura * (3.3 / 4095)  # Convertir a voltaje
            temperatura = voltaje * 100  # LM35 entrega 10mV por grado Celsius
            print("Temperatura:", temperatura, "°C")
            time.sleep(1)
        print("Saliendo del modo temperatura.")
    
    # Primer semáforo en rojo, segundo en verde, tercero en verde, peatonales sincronizados
    led_rojo_1.value(1)
    led_amarillo_1.value(0)
    led_verde_1.value(0)
    led_rojo_2.value(0)
    led_amarillo_2.value(0)
    led_verde_2.value(1)
    led_rojo_3.value(0)
    led_amarillo_3.value(0)
    led_verde_3.value(1)
    peatonal_rojo_1.value(0)
    peatonal_verde_1.value(1)
    peatonal_rojo_2.value(1)
    peatonal_verde_2.value(0)
    time.sleep(3)
    
    # Amarillo en el segundo y tercer semáforo (transición a rojo)
    led_rojo_2.value(0)
    led_amarillo_2.value(1)
    led_verde_2.value(0)
    led_rojo_3.value(0)
    led_amarillo_3.value(1)
    led_verde_3.value(0)
    time.sleep(1)
    
    # Segundo y tercer semáforo en rojo
    led_rojo_2.value(1)
    led_amarillo_2.value(0)
    led_verde_2.value(0)
    led_rojo_3.value(1)
    led_amarillo_3.value(0)
    led_verde_3.value(0)
    time.sleep(1)
    
    # Amarillo en el primer semáforo (transición a verde)
    led_rojo_1.value(1)
    led_amarillo_1.value(1)
    led_verde_1.value(0)
    time.sleep(1)
    
    # Segundo y tercer semáforo en rojo, primero en verde, peatonales sincronizados
    led_rojo_1.value(0)
    led_amarillo_1.value(0)
    led_verde_1.value(1)
    peatonal_rojo_1.value(1)
    peatonal_verde_1.value(0)
    peatonal_rojo_2.value(0)
    peatonal_verde_2.value(1)
    time.sleep(5)
    
    # Amarillo en el primer semáforo (transición a rojo)
    led_rojo_1.value(0)
    led_amarillo_1.value(1)
    led_verde_1.value(0)
    time.sleep(1)
    
    # Primer semáforo en rojo
    led_rojo_1.value(1)
    led_amarillo_1.value(0)
    led_verde_1.value(0)
    time.sleep(1)
    
    # Amarillo en el segundo y tercer semáforo (transición a verde)
    led_rojo_2.value(1)
    led_amarillo_2.value(1)
    led_verde_2.value(0)
    led_rojo_3.value(1)
    led_amarillo_3.value(1)
    led_verde_3.value(0)
    time.sleep(1)
    
    # Si se ha solicitado cruce peatonal, activarlo al final del ciclo
    if solicitar_cruce:
        solicitar_cruce = False
        led_rojo_1.value(1)
        led_rojo_2.value(1)
        led_rojo_3.value(1)
        led_amarillo_1.value(0)
        led_amarillo_2.value(0)
        led_amarillo_3.value(0)
        led_verde_1.value(0)
        led_verde_2.value(0)
        led_verde_3.value(0)
        peatonal_rojo_1.value(0)
        peatonal_verde_1.value(1)
        peatonal_rojo_2.value(0)
        peatonal_verde_2.value(1)
        time.sleep(6)
        # Restaurar los semáforos a su ciclo normal