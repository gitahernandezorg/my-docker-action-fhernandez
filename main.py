import os
print("Python Execution")
token = os.getenv('INPUT_GITHUB-TOKEN')
who = os.getenv('INPUT_WHO-TO-GREET')
print(f"Got token {token}")
print(f"who {who}")

