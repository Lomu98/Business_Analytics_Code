
import requests
import json


url = "https://api.jsonbin.io/b/61cad7b3c277c467cb377947/latest"

payload = json.dumps([
  []
])
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


data =response.json()


with open("the_savings.json", "w") as outfile:
    json.dump(data, outfile)








 

