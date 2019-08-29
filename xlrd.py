import csv 

filename = "ex1.csv"
fields = [] 
rows = [] 
  
with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)  
    fields = next(csvreader) 
    for row in csvreader: 
        rows.append(row) 
  
num = len(rows)
print('\nFirst 5 rows are:\n') 
for row in rows[:num]: 
    print(row[0],row[2])