import json

print("break")

with open("/Users/ikshulbethur/Documents/Projects/ML-Library/json_files/testNetworkData.json", 'r') as f:
    networkData = json.load(f)

with open("Data.json", "w") as e:
    json.dump(networkData, e)

print(networkData['L1'])

f.close()