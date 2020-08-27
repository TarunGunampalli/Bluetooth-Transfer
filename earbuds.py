#!/usr/bin/env python3
import requests
#from bluetool import Bluetooth

#bluetooth = Bluetooth()
#bluetooth.scan()
#print(bluetooth.get_connected_devices())
#print(bluetooth.disconnect("00:02:5b:26:69:96"))

import bluetooth

url = 'https://llamalab.com/automate/cloud/message'
myobj = {
  "secret": "2.aOUxQA1LGBnHasu7PQ1dykr5HQOEEPLaGEpa1gXOZvY",
  "to": "tarun.gunampalli@gmail.com",
  "priority": "normal",
  "payload": "flow;/flows/91/statements/1"
}

x = requests.post(url, json = myobj)

#print(x.text)