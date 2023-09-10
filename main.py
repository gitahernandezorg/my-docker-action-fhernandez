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
 

num = 2 * 2
set_github_action_output('test_variable', num)

multiline = "geeksy\
for\
geeks"
set_github_action_output('multiline', multiline)




