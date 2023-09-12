import os
import uuid
import requests
from sayhellopackagefhernandez import hello

hello.sayhello()

print("Python Execution")
token = os.getenv('INPUT_GITHUB_TOKEN')
greet_env = os.getenv('who-to-greet-env')
print(f"Got token {token}")
print(f"greet_env {greet_env}")


def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()

def set_multiline_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)

"""
num = 2 * 2
set_github_action_output('test_variable', num)
"""

multiline = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

#set_multiline_output('multiline', multiline)

content = "variable content"
#set_multiline_output('test_variable', content)

print(multiline)
print(content)




random_uuid = uuid.uuid4()
secret_name = "my_secret_"+str(random_uuid).replace("-", "")
secret_value = "test_secret_content"

from base64 import b64encode
from nacl import encoding, public

def encrypt(public_key: str, secret_value: str) -> str:
  """Encrypt a Unicode string using the public key."""
  public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
  sealed_box = public.SealedBox(public_key)
  encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
  return b64encode(encrypted).decode("utf-8")

def get_key(url):
    get_key_id_url = "https://api.github.com" + url
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(get_key_id_url, headers=headers)
    key = response.json()
    key_id = key['key_id']
    key_value = key['key']
    print(key)
    return key_id, key_value

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}


key_id, key_value = get_key("/orgs/gitahernandezorg/actions/secrets/public-key")
encrypted_value = encrypt(key_value, f"{secret_name}_ORG")

url = f"https://api.github.com/orgs/gitahernandezorg/actions/secrets/{secret_name}_ORG"
data = {
    "encrypted_value": encrypted_value,
    "visibility":"all",
    "key_id": key_id
}

response = requests.put(url, json=data, headers=headers)
print(response.status_code)
print(secret_name)


key_id, key_value = get_key("/repositories/687137559/environments/dev/secrets/public-key")
encrypted_value = encrypt(key_value, f"{secret_name}_ENV")

url = f"https://api.github.com/repositories/687137559/environments/dev/secrets/{secret_name}_ENV"
data = {
    "encrypted_value": encrypted_value,
    "key_id": key_id
}

response = requests.put(url, json=data, headers=headers)
print(response.status_code)
print(secret_name)

key_id, key_value = get_key("/repos/gitahernandezorg/my-docker-action-fhernandez/actions/secrets/public-key")
encrypted_value = encrypt(key_value, f"{secret_name}_REPO")

url = f"https://api.github.com/repos/gitahernandezorg/my-docker-action-fhernandez/actions/secrets/{secret_name}_REPO"
data = {
    "encrypted_value": encrypted_value,
    "key_id": key_id
}

response = requests.put(url, json=data, headers=headers)
print(response.status_code)
print(secret_name)

