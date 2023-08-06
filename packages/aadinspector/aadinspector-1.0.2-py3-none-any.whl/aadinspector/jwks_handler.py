import json
import requests

DISCOVERY_ENDPOINT = "https://login.microsoftonline.com/{tenant_id}/.well-known/openid-configuration"
JWKS_URI = "https://login.microsoftonline.com/{tenant_id}/discovery/keys?p={name_of_policy}"


class JWKSHandler(object):
    def __init__(self, tenant_id, name_of_policy=""):
        self.tenant_id = tenant_id
        self.name_of_policy = name_of_policy

    def set_tenant(self, tenant_id):
        self.tenant_id = tenant_id

    def set_name_of_policy(self, name_of_policy):
        self.name_of_policy = name_of_policy

    def get_json_from_http_url(self, url):
        response = requests.get(url)
        return json.loads(response.text)

    def get_jwks_uri(self):
        if not self.name_of_policy:
            discovery_url = DISCOVERY_ENDPOINT.format(tenant_id=self.tenant_id)
            response_json = self.get_json_from_http_url(discovery_url)
            return response_json["jwks_uri"]
        else:
            return JWKS_URI.format(tenant_id=self.tenant_id, name_of_policy=self.name_of_policy)

    def get_jwks_keys(self):
        jwks_uri = self.get_jwks_uri()
        response_json = self.get_json_from_http_url(jwks_uri)
        return response_json["keys"]

