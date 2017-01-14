# humidity controller

My stuff:
* Wemo switch (http://www.belkin.com/us/p/P-F7C027/).
* One BeeWi temperature & humidity sensor http://www.bee-wi.com/bbw200,us,4,BBW200-A1.cfm.
* Raspberry Pi 3

Idea: Switch on dehumidifier when humidity is over threshold. Switch off when it's below threshold
## dependecies
```
pip install
npm install
```
## scripts
### reader.js
* it reads temperature and humidity from my BeeWi sensor via BTLE

### dehumidifier.py
* Reads humidity from reader.js and triggers the switch
* This script will be running within crontab

## crontab example
```
*/1 * * * *     /mnt/media/projects/hum/dehumidifier.py ff:ff:ff:ff:ff:ff Switch1 50
```
