from machine import Pin
import time

# Definir los pines para los LEDs del semáforo vehicular
led_rojo = Pin(15, Pin.OUT)
led_amarillo = Pin(2, Pin.OUT)
led_verde = Pin(4, Pin.OUT)

# Definir los pines para los LEDs del semáforo peatonal
peatonal_rojo = Pin(5, Pin.OUT)
peatonal_verde = Pin(18, Pin.OUT)

while True:
    # Rojo encendido (peatonal verde encendido)
    led_rojo.value(1)
    led_amarillo.value(0)
    led_verde.value(0)
    peatonal_rojo.value(0)
    peatonal_verde.value(1)
    time.sleep(3)
    
    # Rojo apaga y amarillo encendido (transición a verde)
    led_rojo.value(0)
    led_amarillo.value(1)
    led_verde.value(0)
    peatonal_rojo.value(1)
    peatonal_verde.value(0)
    time.sleep(1)
    
    # Verde encendido (peatonal rojo encendido)
    led_rojo.value(0)
    led_amarillo.value(0)
    led_verde.value(1)
    peatonal_rojo.value(1)
    peatonal_verde.value(0)
    time.sleep(3)
    
    # Verde apaga y amarillo encendido (transición a rojo)
    led_rojo.value(0)
    led_amarillo.value(1)
    led_verde.value(0)
    peatonal_rojo.value(1)
    peatonal_verde.value(0)
    time.sleep(1)