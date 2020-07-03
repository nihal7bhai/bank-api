import os
import csv
from bankApi.models import Bank
with open(r'bank_branches.csv',encoding="utf8") as f:
    reader = csv.reader(f)
    r=0
    for row in reader:
        try:   
            if(r==0):
                r=1
                continue
            print(row[0])
            created = Bank(
                ifsc=row[0],
                bank_id=row[1],
                branch=row[2],
                address=row[3],
                city=row[4],
                district=row[5],
                state=row[6],quit()
                name=row[7]
                )
            created.save()
        except:
            print('lol')
            pass
