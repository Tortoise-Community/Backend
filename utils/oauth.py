import requests
from django.conf import settings


class Oauth(object):
    client_id = settings.OAUTH_CLIENT_ID
    client_secret = settings.OAUTH_CLIENT_SECRET
    scope = "identify%20email"
    redirect_uri = "https://www.tortoisecommunity.com/verification/handlers/"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"

    def __init__(self, redirect_uri="https://www.tortoisecommunity.com/verification/handlers/"):
        self.redirect_uri = redirect_uri
        self.discord_login_url = "https://discord.com/api/oauth2/authorize?client_id={}&" \
                        "redirect_uri={}&response_type=code&scope={}".format(self.client_id,
                                                                             self.redirect_uri,
                                                                             self.scope)

    def get_access_token(self, code):
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri,
            'scope': self.scope
        }

        headers = {
         'Content-Type': 'application/x-www-form-urlencoded'
        }

        access_token = requests.post(url=self.discord_token_url, data=payload, headers=headers)
        json = access_token.json()
        return json.get("access_token")

    def get_user_json(self, access_token):
        url = self.discord_api_url + '/users/@me'

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }
        user_object = requests.get(url=url, headers=headers)
        user_json = user_object.json()
        return user_json
