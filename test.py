import requests

url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

headers = {
    "accept": "application/json",
    "X-RapidAPI-Key": "3b57dcaa98msh8d23e9f272ba4b4p1f0c91jsn89e23af7bdaf",
    "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
