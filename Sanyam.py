import nexmo
from pprint import pprint

client = nexmo.Client(
  application_id='e6f960ee-334c-43be-a97b-2f81d2d67d5b',
  private_key='./private.key',
)

ncco = [
{
'action': 'talk',
'voiceName': 'Brian',
'text': "Hey Sanyam, Register for server devlopment on cloud. bye"
}
]
response = client.create_call({
'to': [{
'type': 'phone',
'number': '‪918528212201‬'
}],
'from': {
'type': 'phone',
'number': '919492671016'
},
'ncco': ncco
})

pprint(response)
