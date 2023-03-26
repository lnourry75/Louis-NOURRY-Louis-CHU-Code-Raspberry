from machine import Pin
import time
import network
import urequests
import utime
import ujson

led1 = Pin(15, mode=Pin.OUT)
led2 = Pin(14, mode=Pin.OUT)
led3 = Pin(13, mode=Pin.OUT)

pin_button = Pin(18, mode=Pin.IN, pull=Pin.PULL_UP)

trig = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN, Pin.PULL_DOWN)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'iPhone de Louis'
password = '4ujP-C2ab-9m5S-uSXo'
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("pas co")
    pass
    print ('Distance:',"{:.0f}".format(distance),'cm')
    time.sleep(1)
    
    
    
    trig.value(0)
    time.sleep(0.1)
    trig.value(1)
    time.sleep_us(2)
    trig.value(0)
    while echo.value()==0:
        
        pulse_start = time.tick_us()
    while echo.value()==1:
        pulse_end = time.ticks_us()
    pulse_duration = pulse_end - pulse_start
    distance2 = pulse_duration * 17165 / 1000000
    distance 2 = round(distance2, 0)
    dist = abs(distance - distance2)
    print ('Distance: ',"{:.0f}".format(distance2),'cm')
    print ('Vitesse : ',"{:.0f}".format(dist), 'cm/s' )
    
while True:
    print('En attente de presser du bouton')
    while pin_button.value() == 1:
        time.sleep(0.1)
    print('Bouton pressé, démarrage du code')
    led3.on()
    time.sleep(1)
    led3.off()
    lef1.on()
    time.sleep(1)
    led1.off()
    led2.on()
    trig.value(0)
    time.sleep(0.1)
    trig.value(1)
    time.sleep_us(2)
    trig.value(0)
    
    while echo.value()==0:
        pulse_start = time.tick_us()
    while echo.value()==1:
        pulse_end = time.tick_us()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17165 / 1000000
    distance = round(distance, 0)
    
    url = 'http://172.20.10.2:8000/time'
    headers = {'Content-Type': 'application/json'}
    data = {'vitesse': dist}
    response = urequests.post(url, headers=headers, json=data)
    print(response.text)
    led2.off()
    time.sleep(1)