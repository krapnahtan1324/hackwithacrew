import requests

BASE = "http://127.0.0.1:5000/"

user_data = [{'name': 'John', 'email': 'john@email.com', 'password': 'password123'},
            {'name': 'Andrew', 'email': 'andrew@email.com', 'password': 'password123'},
            {'name': 'Katie', 'email': 'katie@email.com', 'password': 'password123'}]


for i in range(len(user_data)):
    response = requests.post(BASE + "users/", user_data[i])
    print(response.json())


input()
response = requests.get(BASE + "/users/0")
print(response.json())