import os
CREDENTIAL_SCOPES =[
    'https://www.googleapis.com/auth/drive'
]
BASE_DIR = os.path.dirname(__file__)
CREDENTIAL_PATH = os.path.join(BASE_DIR, "credential.json")