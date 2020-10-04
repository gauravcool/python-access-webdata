import json

data = '''{
    "name": "Gaurav",
    "phone": {
        "type": "intl",
        "number": "+91-9964229574"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data)
print("Name:", info["name"])
print("Hide:", info["email"]["hide"])