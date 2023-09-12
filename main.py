import os
import uuid
from sayhellopackagefhernandez import hello
from sayhellopackagefhernandezv2 import hello as hello2

print("Hello from sayhellopackagefhernandez")
hello.sayhello()
print("Hello from sayhellopackagefhernandezv2")
hello2.sayhello()

print("Python Execution")
token = os.getenv('INPUT_GITHUB_TOKEN')
greet_env = os.getenv('who-to-greet-env')
print(f"Got token {token}")
print(f"greet_env {greet_env}")

def set_multiline_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)


multiline = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

set_multiline_output('multiline', multiline)

content = "variable content"
set_multiline_output('test_variable', content)



