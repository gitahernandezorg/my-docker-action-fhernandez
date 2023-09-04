import os
print("Python Execution")
token = os.getenv('INPUT_GITHUB_TOKEN')
print(f"Got token {token}")


import requests

url = 'https://api.github.com/orgs/gitahernandezorg/actions/secrets'
headers = {'Authorization': f"token {token}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error al hacer la solicitud:', response.status_code)
