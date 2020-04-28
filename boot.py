# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import gc
import uos, machine
from machine import Pin
esp.osdebug(None)
#uos.dupterm(None, 1) # disable REPL on UART(0)
import network
import webrepl
webrepl.start()
gc.collect()

#Network
#ssid = "SSID"
#password = "password"

#Network Module for Wifi Connection
sta_if = network.WLAN(network.STA_IF)
#sta_if = network.WLAN(network.AP_IF)
sta_if.active(True)
sta_if.connect('MySpectrumWiFi5b-2G', 'jacketreview734')
while sta_if.isconnected() == False:
    pass
print("Connection Succesful")
print(sta_if.ifconfig())

