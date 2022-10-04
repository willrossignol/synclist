import requests
import spotify_auth
import soundcloud_auth

spotify_caller = spotify_auth.spotifyCaller()

def listPlaylists():
    playlists = spotify_caller.session.get(base_url + "me/playlists").json()
    print('-------------------------------')
    for item in playlists['items']:
        print(item['name'])

def showLoggedIn():
    print('Choose an option:\n')
    print('1. List all playlists\n')

def showLoggedOut():
    # Logged in status for spotify account
    print('Spotify account: ', end='')
    if (spotify_caller.checkAccessTokenValid()):
        print('Logged in')
    else:
        print('Not logged in')
    print('-------------------------------')
    print('1. Log into spotify account\n')
    try:
        code = int(input('Enter a choice: '))
    except ValueError:
        return
    handleChoice(code, False)

def showMainMenu():
    print('-------------------------------')
    showLoggedOut()

def handleChoice(choice, loggedIn):
    if not loggedIn:
        if choice == 1:
            spotify_caller.getAccessToken()
            return
    if loggedIn:
        if (choice == 1):
            listPlaylists()
            return

# INFO
base_url = 'https://api.spotify.com/v1/'

# Main Menu
while True:
    showMainMenu()
