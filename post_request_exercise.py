import requests

server_name = "http://vcm-21170.vm.duke.edu:5000/"

request_json = {"name": "Stevan Kriss",
                 "net_id": "sak73",
                 "e-mail": "stevan.kriss@duke.edu"}

r = requests.post(server_name + "student", json = request_json)
