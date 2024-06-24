import os

# Check if the file '.terraform-version' exists
if os.path.isfile('.terraform-version'):
    with open('.terraform-version', 'r') as file:
        version = file.read().strip()
    print(version)
else:
    print("Not Found")