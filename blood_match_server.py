import requests
import json

server_name = " http://vcm-7631.vm.duke.edu:5002/"

r1 = requests.get(server_name + "get_patients/sak73")
# print(r1.text)
ID_dict = json.loads(r1.text)
# print(ID_dict, type(ID_dict))
ID1 = ID_dict["Donor"]
ID2 = ID_dict["Recipient"]
# print(ID1, ID2)

r2 = requests.get(server_name + "get_blood_type/" + ID1)
r3 = requests.get(server_name + "get_blood_type/" + ID2)
bt_donor = r2.text
bt_recipient = r3.text
# print(bt_donor, type(bt_donor))
# print(bt_recipient, type(bt_recipient))

acceptable_match = []

if bt_donor == "A+" and bt_recipient == "A+" or bt_recipient == "AB+":
    acceptable_match = "Yes"
elif bt_donor == "O+" and bt_recipient == "O+" or bt_recipient == "A+" or bt_recipient == "B+" or bt_recipient == "AB+":
    acceptable_match = "Yes"
elif bt_donor == "B+" and bt_recipient == "B+" or bt_recipient == "AB+":
    acceptable_match = "Yes"
elif bt_donor == "AB+" and bt_recipient == "AB+":
    acceptable_match = "Yes"
elif bt_donor == "A-" and bt_recipient == "A+" or bt_recipient == "A-" or bt_recipient == "AB+" or bt_recipient == "AB-":
    acceptable_match = "Yes"
elif bt_donor == "O-":
    acceptable_match = "Yes"
elif bt_donor == "B-" and bt_recipient == "B+" or bt_recipient == "B-" or bt_recipient == "AB+" or bt_recipient == "AB-":
    acceptable_match = "Yes"
elif bt_donor == "AB-" and bt_recipient == "AB+" or bt_recipient == "AB-":
    acceptable_match = "Yes"
else:
    acceptable_match = "No"

print(acceptable_match)

request_json = {"Name": "sak73",
                "Match": acceptable_match}

r4 = requests.post(server_name + "match_check", json=request_json)
print(r4.text)
