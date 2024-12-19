# zoho_integration/api/authentication.py

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class SecretKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        secret_key = request.headers.get('X-Secret-Key')
        if secret_key != 'some-secret-key-would-be-from-vault':  # Replace with actual secret key
            raise AuthenticationFailed('Invalid secret key')
        return None  # Authentication passed
