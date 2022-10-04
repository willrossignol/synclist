import webbrowser
import base64
from urllib.parse import urlencode
import requests
from dotenv import load_dotenv
import os

class spotifyCaller:
    session = requests.session()
    access_token = ""

    def checkAccessTokenValid(self):
        if (not self.access_token):
            return False
        return True

    def getAccessToken(self):
        auth_url = 'https://accounts.spotify.com/authorize'
        redirect_uri = 'https://httpbin.org/cookies/set'

        # Fetch client ID and client secret from .env file
        load_dotenv()
        client_id = os.environ.get('spotifyClientId')
        client_secret = os.environ.get("spotifyClientSecret")

        # Get auth code
        params = {
            "client_id": client_id,
            "response_type": "code",
            "redirect_uri": redirect_uri,
            "scope": "playlist-read-private playlist-modify-private"
        }

        auth_url = auth_url + '?' + urlencode(params)
        webbrowser.open(auth_url)

        code = input('Enter the code: ')

        # Request access token
        params = {
            "code": code,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        }

        authHeader = client_id + ":" + client_secret
        b64Auth = base64.b64encode(authHeader.encode()).decode()

        token_url = 'https://accounts.spotify.com/api/token'
        response = requests.post(token_url, params=params, headers={
            'Authorization': 'Basic %s' % b64Auth,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        )

        # Check if access token request successful
        if (response.status_code != 200):
            print('\nError. Status code: ' + str(response.status_code))
            self.access_token = ""
            return

        print('\nOK. Status code: ' + str(response.status_code) + '\n')
        self.access_token = response.json()['access_token']
        self.session.headers = {'Authorization': f"Bearer {self.access_token}"}