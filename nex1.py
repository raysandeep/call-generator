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
    'text': 'Hey Anusha, You are a bitch.'
  }
]
response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': '917607000863'
  }],
  'from': {
    'type': 'phone',
    'number': '919492671016'
  },
  'ncco': ncco
})

pprint(response)