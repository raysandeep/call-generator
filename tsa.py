import nexmo
from pprint import pprint
from datetime import datetime
from pytz import timezone
import time
client = nexmo.Client(
  application_id='e6f960ee-334c-43be-a97b-2f81d2d67d5b',
  private_key='./private.key',
)




#monday=0,wednesday=2,friday=4

while(True):
    count = 0
    format = "%Y-%m-%d %H:%M:%S %Z%z"
    now_utc = datetime.now(timezone('UTC'))
    now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
    nw = now_asia.strftime(format)
    print(nw)
    hour = int(nw.split(" ")[1].split(":")[0])
    minute = int(nw.split(" ")[1].split(":")[1])
    second = int(nw.split(" ")[1].split(":")[2])
    time.sleep(0.9)

    #print("test")
    while(hour == 6 and minute == 54 and second == 00):
        print("test-2")
        if(count<1):
            ncco = [
            {
                'action': 'talk',
                'voiceName': 'Salli',
                'text': "Hey Pranavi, This a automatic call generated by sandeep. Wake up at 9 am you have digital circuit design class. thank you. bye"
            }
            ]
            response = client.create_call({
            'to': [{
                'type': 'phone',
                'number': '919492671016'
            }],
            'from': {
                'type': 'phone',
                'number': '919492671016'
            },
            'ncco': ncco
            })

            pprint(response)
            
            break
    while(hour == 6 and minute == 56 and second == 00):
        print("test-2")
        if(count<1):
            ncco1 = [
            {
                'action': 'talk',
                'voiceName': 'Salli',
                'text': "Hey Pranavi, This a automatic call generated by sandeep. Wake up at 9 am you have digital circuit design class. thank you. bye"
            }
            ]
            response1 = client.create_call({
            'to': [{
                'type': 'phone',
                'number': '919492671016'
            }],
            'from': {
                'type': 'phone',
                'number': '919492671016'
            },
            'ncco': ncco1
            })

            pprint(response1)
            
            break

