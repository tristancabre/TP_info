import requests

response = requests.get("https://swapi.info/api/people")

print(response.json())

response2 = requests.get("https://swapi.info/api/people/51")

print(response2.json())
