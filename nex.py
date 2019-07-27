import nexmo
from pprint import pprint

client = nexmo.Client(
  application_id='e6f960ee-334c-43be-a97b-2f81d2d67d5b',
  private_key='./private.key',
)
ncco = [
  {
    'action': 'talk',
    'voiceName': 'Salli',
    'text': "Hey Saniya, I'm the guy that confessed to you over Instagram. I waited a really long time for you at FC but you didn't show up. I'll keep waiting for you every Friday at 6. Please understand that I really like you and I'd wait for two more years if I have to"
  }
]
response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': '919561535666'
  }],
  'from': {
    'type': 'phone',
    'number': '919492671016'
  },
  'ncco': ncco
})

pprint(response)