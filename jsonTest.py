import json

print("break")

f = open('json_files/testNetworkData.json')

networkData = json.load(f)

for i in networkData['L2']:
    dat = i['N1']
    print(dat['w'])

f.close()