import jwt

class JWTValidator(object):
    def __init__(self,public_key):
        self.public_key = public_key
    
    def validate(self, token):
        try:
            jwt_unverified = jwt.decode(
                token, options={"verify_signature": False})
            iss = jwt_unverified["iss"]
            aud = jwt_unverified["aud"]
            decoded = jwt.decode(token,
                                 self.public_key,
                                 verify=True,
                                 algorithms=['RS256'],
                                 audience=aud,
                                 issuer=iss)
            return (True, decoded)
        except Exception as e:
            print(e)
            return(False, e)