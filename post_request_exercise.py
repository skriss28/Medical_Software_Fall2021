import requests

server_name = "http://vcm-21170.vm.duke.edu:5000/"

request_json1 = {"name": "Stevan Kriss",
                 "net_id": "sak73",
                 "e-mail": "stevan.kriss@duke.edu"}

request_json2 = {"a": 1,
                 "b": 2}

r1 = requests.post(server_name + "student", json=request_json1)
r2 = requests.get(server_name + "list")
r3 = requests.post(server_name + "sum", json=request_json2)

print(r1.text)
print(r2.text)
print(r3.text)
