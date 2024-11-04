import json
import os
import requests

# Setup Configuration
f = open('./config.json', 'r')
config = json.loads(f.read())
print("Configuration File:")
print(json.dumps(config, indent=4))
f.close()

# Get Stop Info
def getStop(stopId:int):
    request = requests.get(
        url=f"https://api.actransit.org/transit/stops/{stopId}/predictions?token={config['actransit']['apikey']}")
    if request.status_code == 200:
        print(json.dumps(request.json(),indent=4))
    elif request.status_code == 400:
        print("No predictions")
    else:
        print(f"Stop Lookup for {stopId} Failed")
        print(request)

# Testing
getStop(55167)
[getStop(stopId) for stopId in config['actransit']['stopsOfInterest']]