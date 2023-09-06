import os
import base64
import requests
import uuid


print("Python Execution")
token = os.getenv('INPUT_GITHUB_TOKEN')
greet_env = os.getenv('who-to-greet-env')
print(f"Got token {token}")
print(f"greet_env {greet_env}")


def set_github_action_output(output_name, output_value):
    print("GITHUB_OUTPUT", os.environ["GITHUB_OUTPUT"])
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()


""""
url = 'https://api.github.com/orgs/gitahernandezorg/actions/secrets'
headers = {'Authorization': f"token {token}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error al hacer la solicitud:', response.status_code)
"""
num = 2 * 2
set_github_action_output('test_variable', num)

multiline = "geeksy\
for\
geeks"
set_github_action_output('multiline', multiline)

""""
random_uuid = uuid.uuid4()

# Definir los parámetros necesarios
secret_name = "my_secret_"+str(random_uuid).replace("-", "")
secret_value = multiline  # El valor del secreto que deseas almacenar


# URL de la API de GitHub para crear el secreto
url = f"https://api.github.com/orgs/gitahernandezorg/actions/secrets/{secret_name}"

get_key_id_url = f"https://api.github.com/orgs/gitahernandezorg/actions/secrets/public-key"

# Configura los encabezados de la solicitud
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.get(get_key_id_url, headers=headers)

key_id_data = response.json()

secret_value_base64 = base64.b64encode(secret_value.encode()).decode()

data = {
    "encrypted_value": secret_value_base64,
    "visibility":"selected",
    "key_id": key_id_data['key_id']
}

# Realiza la solicitud POST para crear el secreto
response = requests.put(url, json=data, headers=headers)

# Verifica la respuesta de la solicitud
if response.status_code == 201:
    print(f"Secrete was created: {secret_name}")
else:
    print(f"No se pudo crear el secreto. Código de estado: {response.status_code}")
    print(f"Respuesta: {response}")
"""