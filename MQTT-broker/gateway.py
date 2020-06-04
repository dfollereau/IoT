import hashlib;
import hmac;
import datetime;
import paho.mqtt.client as mqtt
import json
import calendar
import requests
from datetime import date
from datetime import datetime

mqqt_server = '192.168.1.73' #IP allocated by you or your DHCP/Box for the MQTT gateway
mqqt_port = 1883

def on_connect(mqttc, obj, flags, rc):
    #print("Connected with result code "+str(rc))
    client.subscribe("/iotdemo/temp")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    v=str(msg.payload.decode('utf8'))
    #string comes in as bytes so need to convert it
    sample=json.loads(v)

    time_t = datetime.now()
    timestamp_utc = calendar.timegm(time_t.timetuple())

    #print('Processing sample : ' + str(sample['value']))

    body='{ "device":"' + str(sample['device']) + '", "sample_date" : "' + time_t.strftime("%Y-%m-%d") + '", "value":"' + str(sample['value']) + '", "time":"' + repr(timestamp_utc) + '" }'
    print("Message: " + body)
    secret = 'xxxxxx' #'MongoDB Stitch Webhook password here'
    hash = hmac.new(bytes(secret, 'latin-1'), body.encode("utf-8"), hashlib.sha256)
    url = 'https://webhooks.mongodb-stitch.com/api/client/v2.0/app/connecteddevices-xmzek/service/iotreceivedata/incoming_webhook/savesensordata' #enter your Stitch Web API URL here
    header={"Content-Type":"application/json","X-Hook-Signature":"sha256=" + hash.hexdigest()  }
    myResponse = requests.post(url,headers=header, data=body )
    #print (myResponse.status_code)


# uncomment to debug
#def on_log(mqttc, obj, level, string):
#    print(string)

#print('Connecting to MQQT broker')
client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect
#client.on_log = on_log
client.connect(mqqt_server, mqqt_port, 60)
client.loop_forever()

