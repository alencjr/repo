import requests 

res = requests.get("https://www.google.com")
resjs = res.json()
print(resjs.text())
