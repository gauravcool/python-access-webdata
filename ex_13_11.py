import json

data = '''[
    {
        "name": "Gaurav",
        "usn": "1PI10IS034",
        "dob": "31-03-92"
    },
    {
        "name": "Akshay",
        "usn": "1PI10IS009",
        "dob": "01-08-92"
    }
]'''

info = json.loads(data)
for item in info:
    print("Name:", item["name"])
    print("USN:", item["usn"])
    print("Date of Birth:", item["dob"])