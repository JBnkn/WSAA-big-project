import requests
import mysql.connector
import lastfmapi as api

api_key = api.lastfm['api']

conn = mysql.connector.connect(
    host= api.mysql['host'],
    user= api.mysql['user'],
    password= api.mysql['password'],
    database=api.mysql['database']
)
cursor = conn.cursor()

topartists = f"http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={api_key}&format=json"
response = requests.get(topartists)
data = response.json()

for artist in data['artists']['artist']:
    print(artist['name'])
