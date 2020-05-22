## NodeMCU Web server with LED on/Off button
The webser demo can be seen here:
https://youtu.be/HBPcY_rqhq0

### Configuring The NodeMCU:
Prerequisites require adding the devices group to your username, python, micropython, pip (a package manager for python), picocom (for connecting to the microcontroller), and the firmware for the board found at http://micropython.org/download#esp8266. I also recommend following the micropython documentation while configuring the micro-controller; https://docs.micropython.org/en/latest/ .  

Once everything is installed and the firmware file is downloaded, the following commands are run to update the firmware:
```bash
$ls -l /dev/ttyACM*
crw-rw---- 1 root <groupname> ttyACM0 
```
Add your username to the groupname of the device, and then run the commands after the groupadd.
```bash
sudo usermod -a -G dialout <username> 
sudo chmod a+rw /dev/ttyACM0
pip install esptool
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=detect 0 /locationwerethefileislocated/esp8266-20170108-v1.8.7.bin
````
After the firmware is updated, you can connect to the device as seen below.

![alt text](https://raw.githubusercontent.com/AnthonyMaz/NodeMCU/master/images/connection.png)

After connecting to the device, the network should be setup as seen to the below. 
![alt text](https://raw.githubusercontent.com/AnthonyMaz/NodeMCU/master/images/netwkcfg.png)

Once it’s seen that the interfaces are active, one can scan for Wifi networks as seen below.
![alt text](https://raw.githubusercontent.com/AnthonyMaz/NodeMCU/master/images/wifiscan.png)

After seeing your network, put in the information below. This can also be found at https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html
```bash
>>> sta_if.connect('<your ESSID>', '<your password>')
```
Once established you can check the IP address:
```bash
>>> sta_if.ifconfig()
('192.168.0.2', '255.255.255.0', '192.168.0.1', '8.8.8.8')
```
You can then disable the access-point interface if you no longer need it:
```bash
>>> ap_if.active(False)
```
Here is a function you can run (or put in your boot.py file) to automatically connect to your WiFi network:
```bash
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<essid>', '<password>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
```

### Implementing a Web Server with the NodeMCU
There are two main scripts that need to be setup after updating the firmware on the 
NodeMCU depending on the purpose of the project on the board. This project is intended to be a Web Server that controls a LED. Those two scripts are as follows:
```bash	
→ boot.py – this script is executed when the board boots up. It sets up various configuration options for the board.
→ main.py – this is the main script that will contain your Python program. It is executed after boot.py.
```
#### Boot.py Configuration:
This script is intended for automatic network configurations, and any needed python libraries to load from boot for other scripts. As seen below, this is the boot configuration I have used. 
![alt text](https://raw.githubusercontent.com/AnthonyMaz/NodeMCU/master/images/bootpy.png)
#### Main.py Configuration:
This script is intended for parts of your python program projects that are running on your board.
For this project, I have included a web server configuration in the Main.py, which can be seen below.
![alt text](https://raw.githubusercontent.com/AnthonyMaz/NodeMCU/master/images/mainpy0.png)
![alt text](https://raw.githubusercontent.com/AnthonyMaz/NodeMCU/master/images/mainpy1.png)
#### Web Server:
Below is a screenshot of the ESP8266 Web Server after configuring the boot.py and main.py files.
![alt text](https://raw.githubusercontent.com/AnthonyMaz/NodeMCU/master/images/webserver.png)
