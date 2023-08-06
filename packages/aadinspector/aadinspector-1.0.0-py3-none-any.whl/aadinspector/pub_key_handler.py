import base64
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import jwt
from jwks_handler import JWKSHandler

class InvalidAuthorizationToken(Exception):
    def __init__(self, details):
        super().__init__('Invalid authorization token: ' + details)
class PublicKeyHandler(object):
    def __init__(self, tenant_id,name_of_policy=""):
        self.tenant_id = tenant_id
        self.name_of_policy = name_of_policy
    
    def set_tenant(self, tenant_id):
        self.tenant_id = tenant_id

    def set_name_of_policy(self, name_of_policy):
        self.name_of_policy = name_of_policy
    
    def get_kid(self, token):
        headers = jwt.get_unverified_header(token)
        if not headers:
            raise InvalidAuthorizationToken('missing headers')
        try:
            return headers['kid']
        except KeyError:
            raise InvalidAuthorizationToken('missing kid')

    def get_jwks_keys(self):
        jwks_handler = JWKSHandler(self.tenant_id, self.name_of_policy)
        return jwks_handler.get_jwks_keys()

    def get_jwk(self, kid):
        jwks = self.get_jwks_keys()
        for jwk in jwks:
            if jwk["kid"] == kid:
                return jwk
        raise InvalidAuthorizationToken('kid not recognized')

    def ensure_bytes(self, key):
        if isinstance(key, str):
            key = key.encode('utf-8')
        return key

    def decode_value(self, val):
        decoded = base64.urlsafe_b64decode(self.ensure_bytes(val) + b'==')
        return int.from_bytes(decoded, 'big')

    def rsa_pem_from_jwk(self, jwk):
        return RSAPublicNumbers(
            n=self.decode_value(jwk['n']),
            e=self.decode_value(jwk['e'])
        ).public_key(default_backend()).public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
    def get_public_key(self, token):
        return self.rsa_pem_from_jwk(self.get_jwk(self.get_kid(token)))
