import requests
import json
response=requests.get("https://api.sampleapis.com/coffee/hot")
data=response.json()
def give_data():
    return data