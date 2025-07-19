from utils.credential_manager import CredentialManager

def test_get_credential():
    # Initialize CredentialManager with a sample config path
    cm = CredentialManager('./credentials.json')
    # Test getting a credential that exists
    credential = cm.get_credential('__SHOPPING__')
    print(f"Credential for __SHOPPING__: {credential}")
    print(f"Credential URL: {credential.get('url')}")
    print(f"Credential Username: {credential.get('username')}")
    print(f"Credential Password: {credential.get('password')}")
    # Test getting a credential that does not exist
    non_existent_credential = cm.get_credential('__NON_EXISTENT__')
    print(f"Credential for __NON_EXISTENT__: {non_existent_credential}")


test_get_credential()