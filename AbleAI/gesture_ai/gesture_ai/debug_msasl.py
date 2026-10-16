import json

with open("data/MS-ASL/MSASL_train.json", "r") as f:
    data = json.load(f)

print("Total entries:", len(data))
print("Keys in first entry:", data[0].keys())
print("First entry sample:")
print(data[0])
