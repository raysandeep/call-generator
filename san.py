import nexmo
from pprint import pprint
from datetime import datetime
from pytz import timezone

client = nexmo.Client(
  application_id='e6f960ee-334c-43be-a97b-2f81d2d67d5b',
  private_key='./private.key',
)



dt=datetime.datetime.today()
print(dt.weekday())
#monday=0,wednesday=2,friday=4

while(True):
    count = 0
    format = "%Y-%m-%d %H:%M:%S %Z%z"
    now_utc = datetime.now(timezone('UTC'))
    now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
    nw = now_asia.strftime(format))

    #print("test")
    while(nw.hour == 8 and nw.minute == 00 and nw.second == 00):
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
                'number': '919491263795'
            }],
            'from': {
                'type': 'phone',
                'number': '919492671016'
            },
            'ncco': ncco
            })

            pprint(response)
            
            break
    while(nw.hour == 8 and nw.minute == 30 and nw.second == 00):
        print("test-2")
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
                'number': '919491263795'
            }],
            'from': {
                'type': 'phone',
                'number': '919492671016'
            },
            'ncco': ncco
            })

            pprint(response)
            
            break
           
