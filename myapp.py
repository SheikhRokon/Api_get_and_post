import requests
import json

Url ="http://127.0.0.1:8000/student_create/"

data={
    'name': 'Sumon',
    'father_name':'Khan',
    'roll': 555,
    'email': 'sdn@gmail.com',
}

json_data=json.dumps(data) #ডাটা কে জেসন ডাটা তে রূপান্তর Convert data to json data
r = requests.post(url=Url, data=json_data)
data_s =r.json()
print(data_s)
