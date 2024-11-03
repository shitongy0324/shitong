import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    joke = data.get("value")
    print("Here's a Chuck Norris joke for you:")
    print(joke)
else:
    print("Failed to retrieve a joke. Please try again later.")
