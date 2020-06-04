# NodeMCU ESP8266 Microcontroller

Extract from: https://en.wikipedia.org/wiki/NodeMCU
<br>
Buy (7 euros): https://www.amazon.fr/dp/B06Y1ZPNMS/ref=cm_sw_em_r_mt_dp_U_5wq2EbJ6V774R

Many kind of sensors having i2c bus can be connected to this microchip. Here I am using C language with Arduino IDE. It is also possible to patch the firmware with Micropython. I tested to patch the firmware with BIN file downloaded from here https://micropython.org/download/esp8266/ but I preferred to continue with a C program being more straight forward for me.

Schematics : VCC/GND and for i2c: D1-SCL and D2-SDA
<img src="../img/esp8266.jpg" width="600" height="400"/>
