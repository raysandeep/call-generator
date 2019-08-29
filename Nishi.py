import nexmo
from pprint import pprint
import csv 

filename = "ex1.csv"
fields = [] 
rows = [] 
client = nexmo.Client(
  application_id='e6f960ee-334c-43be-a97b-2f81d2d67d5b',
  private_key='./private.key',
)

with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)  
    fields = next(csvreader) 
    for row in csvreader: 
        rows.append(row) 
num = len(rows)
print(num)
for row in rows[:num]: 
    #print(row[0],row[2])

    ncco = [
    {
    'action': 'talk',
    'voiceName': 'Brian',
    'text': "Hey"+ row[0] + "Hi How are you??"
    }
    ]
    response = client.create_call({
    'to': [{
    'type': 'phone',
    'number': "91"+str(row[2])
    }],
    'from': {
    'type': 'phone',
    'number': '919492671016'
    },
    'ncco': ncco
    })

    pprint(response)
