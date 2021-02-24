import requests

r = requests.get('http://localhost:8080/name?name=Test')
print(r.text)