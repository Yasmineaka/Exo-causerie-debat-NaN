import requests
requests.get('https://jsonplaceholder.typicode.com/todos/1')
nom = requests.get('https://jsonplaceholder.typicode.com/users')
#print(nom.text)
user = nom.json()
print(user)
for i in user:
    print(i["id"], i["name"])


