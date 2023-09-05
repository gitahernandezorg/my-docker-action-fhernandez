import os
print("Python Execution")
token = os.getenv('INPUT_GITHUB_TOKEN')
greet_env = os.getenv('who-to-greet-env')
print(f"Got token {token}")
print(f"greet_env {greet_env}")


def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()
    

""""
import requests

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

