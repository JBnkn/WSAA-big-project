import requests
import mysql.connector
import lastfmapi as api

# import required information from config file
api_key = api.lastfm['api']
conn = mysql.connector.connect(
    host= api.mysql['host'],
    user= api.mysql['user'],
    password= api.mysql['password'],
    database=api.mysql['database']
)
cursor = conn.cursor()

# pull top 500 artists from lastfm api using params
top500 = f"http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={api_key}&format=json&limit=500"
response = requests.get(top500)
data = response.json()

# extract artist names from json response
for artist in data['artists']['artist']:
    name = artist['name']
    playcount = int(artist['playcount'])
    listeners = int(artist['listeners'])
    url = artist['url']

# work on sql query
    sql = "INSERT INTO artists (mbid, name, playcount, listeners, url) VALUES (%s, %s, %s, %s, %s)