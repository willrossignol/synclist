import webbrowser
import base64
from urllib.parse import urlencode
import requests

def getAccessToken():
    auth_url = 'https://api.soundcloud.com/connect'