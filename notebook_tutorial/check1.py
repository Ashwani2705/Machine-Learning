import json
from kaggle.api.kaggle_api_extended import KaggleApi

# Read the kaggle.json file from the same folder
with open('kaggle.json', 'r') as f:
    kaggle_credentials = json.load(f)

# Extract the username and key
username = kaggle_credentials['username']
key = kaggle_credentials['key']

# Initialize the API object and set the credentials manually
api = KaggleApi()
api.credentials = {
    'username': username,
    'key': key
}

# Authenticate using the manually set credentials
api.authenticate()

# Now you can interact with the Kaggle API
