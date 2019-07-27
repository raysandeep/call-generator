import nexmo
from pprint import pprint
import datetime

client = nexmo.Client(
  application_id='e6f960ee-334c-43be-a97b-2f81d2d67d5b',
  private_key='./private.key',
)

dt=datetime.datetime.today()
print(dt.weekday())

#monday=0,wednesday=2,friday=4

while(True):
    count = 0
    nw=datetime.datetime.now()
    #print("test")
    while(nw.hour == 6 and nw.minute == 30 and nw.second == 00):
        print("test-2")
        if(count<1):
            ncco = [
            {
                'action': 'talk',
                'voiceName': 'Salli',
                'text': "Hey Sandy , Wake upp wake up wake up wake up wake up"
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
            
            ncco1 = [
            {
                'action': 'talk',
                'voiceName': 'Salli',
                'text': "Hey Gollu , Wake upp wake up wake up wake up wake up"
            }
            ]
            response1 = client.create_call({
            'to': [{
                'type': 'phone',
                'number': '917010473891'
            }],
            'from': {
                'type': 'phone',
                'number': '919492671016'
            },
            'ncco': ncco1
            })

            pprint(response1)
            break
    while(nw.hour == 6 and nw.minute == 30 and nw.second == 00):
        print("test-2")
        if(count<1):
            ncco = [
            {
                'action': 'talk',
                'voiceName': 'Salli',
                'text': "Hey Sandy , Wake upp wake up wake up wake up wake up"
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
            
            ncco1 = [
            {
                'action': 'talk',
                'voiceName': 'Salli',
                'text': "Hey Gollu , Wake upp wake up wake up wake up wake up"
            }
            ]
            response1 = client.create_call({
            'to': [{
                'type': 'phone',
                'number': '917010473891'
            }],
            'from': {
                'type': 'phone',
                'number': '919492671016'
            },
            'ncco': ncco1
            })

            pprint(response1)
            break