import json

class CredentialManager:
    def __init__(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get_credential(self, system_name):
        return self.data.get(system_name)
